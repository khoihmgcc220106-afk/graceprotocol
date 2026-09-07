import unicodedata
import re
from underthesea import word_tokenize

class VietnameseTextProcessor:
    """Vietnamese text preprocessing and normalization engine."""

    def __init__(self):
        """Initialize the Vietnamese text processor."""
        pass

    def normalize_unicode(self, text: str) -> str:
        """Normalize input string to Unicode NFC standard form."""
        return unicodedata.normalize('NFC', text)

    def clean_text(self, text: str) -> str:
        """Convert text to lowercase and remove excess whitespace."""
        text = str(text).lower()
        # Replace multiple consecutive whitespaces (spaces, tabs, newlines) with a single space
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def tokenize(self, text: str) -> str:
        """Perform Vietnamese word segmentation using Underthesea library."""
        # Use format="text" to join compound words with underscores (e.g., 'hoc_sinh')
        return word_tokenize(text, format="text")

    def process_pipeline(self, text: str) -> str:
        """Execute the complete normalization and tokenization pipeline sequentially."""
        if not text:
            return ""

        text = self.normalize_unicode(text)
        text = self.clean_text(text)
        text = self.tokenize(text)
        return text
