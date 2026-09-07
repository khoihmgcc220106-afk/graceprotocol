import os
import re
from typing import List, Set

class NLPRuleEngine:
    """Rule-based engine for dictionary lookup and linguistic error detection."""

    def __init__(self, vocab_path: str = None):
        """Initialize the engine and load the vocabulary into memory."""
        self.vocabulary: Set[str] = set()

        # Default to the vocab.txt in the same directory if no path is provided
        if vocab_path is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            vocab_path = os.path.join(current_dir, "vocab.txt")

        self._load_vocabulary(vocab_path)

    def _load_vocabulary(self, file_path: str) -> None:
        """Load words from a text file into a Python set for O(1) lookup."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    word = line.strip()
                    if word:
                        self.vocabulary.add(word.lower())
        except FileNotFoundError:
            print(f"Warning: Vocabulary file not found at {file_path}")

    def is_oov(self, token: str) -> bool:
        """
        Check if a token is Out-Of-Vocabulary (OOV).
        Returns True if the token is NOT in the dictionary.
        """
        # Ignore pure punctuation tokens (e.g., '!', '?', ',')
        if re.match(r'^[^\w\s]+$', token):
            return False

        return token.lower() not in self.vocabulary

    def detect_consonant_errors(self, token: str) -> List[str]:
        """
        Apply deterministic rules to flag potential consonant confusion.
        Example: Flagging 'ch' vs 'tr', 's' vs 'x' for review.
        """
        flags = []
        token_lower = token.lower()

        # Simple heuristic rules for common Vietnamese spelling confusion
        if token_lower.startswith('tr') or token_lower.startswith('ch'):
            flags.append("flag_ch_tr")
        elif token_lower.startswith('s') or token_lower.startswith('x'):
            flags.append("flag_s_x")

        return flags
