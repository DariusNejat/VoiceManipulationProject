# libraries/__init__.py

# Import functions from all libraries
from .library1 import segment_audio_list  # Example function from library1.py
from .library2 import reverse_segments  # Example function from library2.py
from .library3 import manipulate_segments  # Example function from library3.py
from .library4 import save_audio  # Example function from library4.py
from .library5 import smooth_audio_list  # Example function from library5.py
from .library6 import concatenate_segments  # Example function from library6.py
# Add more imports as needed for all libraries

# List of all imported functions (for easier access in main.py)
__all__ = [
    "save_audio",
    "segment_audio_list",
    "reverse_segments",
    "manipulate_segments",
    "smooth_audio_list",
    "concatenate_segments", 
    # Add more functions here as needed
]
