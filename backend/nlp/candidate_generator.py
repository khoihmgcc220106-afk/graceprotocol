from typing import List, Set

class CandidateGenerator:
    """Generates correction candidates for Out-Of-Vocabulary (OOV) words using Edit Distance."""

    def __init__(self, vocabulary: Set[str]):
        """Initialize with a loaded vocabulary set."""
        self.vocabulary = vocabulary

    def _levenshtein_distance(self, s1: str, s2: str) -> float:
        """
        Calculate the Levenshtein distance between two strings with phonetic weighting.
        Returns a float because of fractional phonetic penalties.
        """
        if len(s1) < len(s2):
            return self._levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return float(len(s1))

        previous_row = [float(i) for i in range(len(s2) + 1)]

        # Phonetic confusion pairs in Vietnamese
        phonetic_pairs = [{'s', 'x'}, {'c', 'k'}, {'l', 'n'}, {'t', 'c'}]

        for i, c1 in enumerate(s1):
            current_row = [float(i + 1)]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1.0
                deletions = current_row[j] + 1.0

                # Default substitution cost is 1.0 if characters differ, 0.0 if same
                sub_cost = 0.0 if c1 == c2 else 1.0

                # Apply phonetic weighting (reduce penalty to 0.5) for common confusions
                if c1 != c2 and {c1, c2} in phonetic_pairs:
                    sub_cost = 0.5

                substitutions = previous_row[j] + sub_cost

                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def generate_candidates(self, oov_token: str, top_k: int = 3) -> List[str]:
        """
        Find the top_k closest words in the vocabulary for the given OOV token.
        """
        token_lower = oov_token.lower()
        candidates = []

        for word in self.vocabulary:
            # Optimization: skip words with drastically different lengths to save CPU cycles
            if abs(len(word) - len(token_lower)) > 3:
                continue

            distance = self._levenshtein_distance(token_lower, word)
            candidates.append((word, distance))

        # Sort by distance (ascending) and return the top_k candidates
        candidates.sort(key=lambda x: x[1])
        return [word for word, distance in candidates[:top_k]]
