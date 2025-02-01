# libraries/__init__.py

# Import functions from all libraries
from .library1 import segment_voice  # Example function from library1.py
from .library2 import reverse_segments  # Example function from library2.py
from .library3 import change_pitch  # Example function from library3.py
from .library4 import adjust_speed  # Example function from library4.py
from .library5 import smooth_audio_list  # Example function from library5.py
from .library6 import tone_down  # Example function from library6.py
# Add more imports as needed for all libraries

# List of all imported functions (for easier access in main.py)
__all__ = [
    "segment_voice",
    "reverse_segments",
    "smooth_audio_list",
    "adjust_speed",
    "raise_voice",
    "tone_down",
    # Add more functions here as needed
]
