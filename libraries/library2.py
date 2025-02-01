import re



def pattern_decoder(pattern:str):
    """
    Return the multiplier and the constant in the pattern
     
    Paramaters:
        pattern (str): should follow this pattern: MULT * var * CONS, where var can be any letter and MULT & CONS can be float or int.
        MULT and CONS are required. use 1 * n + 0 if you mean a pattern which only includes n.
    Raises:
        Exception: if the pattern does not match the format, an exception will be raised.

    Returns:
        Multiplier (float): the multiplier in the pattern
        Constant (float): The constant in the pattern
    """
    pattern = pattern.replace(' ','')
    if re.match(r'(\d|\d\.\d)(\*)([a-zA-Z])((\+|\-)(\d|(\d.\d)))', pattern):
        multiplier = float(re.findall(r'(\d|\d\.\d)(\*)([a-zA-Z])((\+|\-)(\d|(\d\.\d)))',pattern)[0][0])
        constant = float(re.findall(r'(\d|\d\.\d)(\*)([a-zA-Z])((\+|\-)(\d\.\d|\d))',pattern)[0][3])
    else:
        raise Exception(f"The pattern: '{pattern}' does not match the following pattern: 'multiplier * n + constant'")
    
    return multiplier,constant


def reverse_segments(segments_list: list,sr,pattern: str):
    
    """
    Reverses the segments whose index follows the pattern.
    
    Parameters:
        segments_list (list): list of the segments/audios. if only one audio is to be reversed, pass it in a list
        pattern (str): the pattern which is used to select the segments. Should follow this pattern: 'MULT * var * CONS', where 'var' can be any letter and 'MULT' & 'CONS' can be float or int. 'MULT and CONS' are required. 
        Use 1 * n + 0 if you mean a pattern which includes all the segments.

    Returns:
        segments_list (list): the list of segments.
    """
    try:
        multiplier, constant = pattern_decoder(pattern)
        i = 0
        while multiplier * i + constant < len(segments_list):
            segments_list[i] = segments_list[i][::-1]
            i += 1
        return segments_list
    except Exception as e:
        raise e
        
