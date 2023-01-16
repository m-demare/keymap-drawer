"""
Module containing configuration related to styling of produced SVG and other drawing options,
keycode converters for parsing.
"""

from textwrap import dedent
from pydantic import BaseSettings


class DrawConfig(BaseSettings):
    """Configuration related to SVG drawing, including key sizes, padding amounts, combo drawing settings etc."""

    # key dimensions, non-ortho layouts use key_h for width as well
    key_w: int = 60
    key_h: int = 56

    # gap between two halves for ortho layout generator
    split_gap: int = key_w / 2

    # combo box dimensions
    combo_w: int = key_w / 2 - 2
    combo_h: int = key_h / 2 - 2

    # curvature of rounded key rectangles
    key_rx: int = 6
    key_ry: int = 6

    # padding between keys
    inner_pad_w: int = 2
    inner_pad_h: int = 2

    # padding between layers
    outer_pad_w: int = key_w / 2
    outer_pad_h: int = key_h

    # spacing between multi-line text in key labels
    line_spacing: int = 18

    # curve radius for combo dendrons
    arc_radius: int = 6

    # length multiplier for dendrons
    arc_scale: float = 1.0

    svg_style: str = dedent(
        """\
        /* font and background color specifications */
        svg {
            font-family: SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;
            font-size: 14px;
            font-kerning: normal;
            text-rendering: optimizeLegibility;
            fill: #24292e;
        }

        /* default key styling */
        rect {
            fill: #f6f8fa;
            stroke: #d6d8da;
            stroke-width: 1;
        }

        /* color accent for held keys */
        .held {
            fill: #fdd;
        }

        /* color accent for combo boxes */
        .combo {
            fill: #cdf;
        }

        /* color accent for ghost (optional) keys */
        .ghost {
            fill: #ddd;
        }

        text {
            text-anchor: middle;
            dominant-baseline: middle;
        }

        /* styling for layer labels */
        .label {
            font-weight: bold;
            text-anchor: start;
            stroke: white;
            stroke-width: 2;
            paint-order: stroke;
        }

        /* styling for combo box label text */
        .small {
            font-size: 80%;
        }

        /* styling for combo dendrons */
        path {
            stroke-width: 1;
            stroke: gray;
            fill: none;
        }
    """
    )


class ParseConfig(BaseSettings):
    """Configuration settings related to parsing QMK/ZMK keymaps."""

    preprocess: bool = True
    skip_binding_parsing: bool = False
    keycode_map: dict[str, str] = {  # pylint: disable=duplicate-key
        # QMK keycodes
        "MINUS": "-",
        "MINS": "-",
        "EQUAL": "=",
        "EQL": "=",
        "LEFT_BRACKET": "[",
        # "LBRC": "[",  confusable with ZMK version
        "RIGHT_BRACKET": "]",
        # "RBRC": "]",  confusable with ZMK version
        "BACKSLASH": "\\",
        "BSLS": "\\",
        "NONUS_HASH": "#",
        "NUHS": "#",
        "SEMICOLON": ";",
        "SCLN": ";",
        "QUOTE": "'",
        "QUOT": "'",
        "GRAVE": "`",
        "GRV": "`",
        "COMMA": ",",
        "COMM": ",",
        "DOT": ".",
        "SLASH": "/",
        "SLSH": "/",
        "TILDE": "~",
        "TILD": "~",
        "EXCLAIM": "!",
        "EXLM": "!",
        "AT": "@",
        "HASH": "#",
        "DOLLAR": "$",
        "DLR": "$",
        "PERCENT": "%",
        "PERC": "%",
        "CIRCUMFLEX": "^",
        "CIRC": "^",
        "AMPERSAND": "&",
        "AMPR": "&",
        "ASTERISK": "*",
        "ASTR": "*",
        "LEFT_PAREN": "(",
        "LPRN": "(",
        "RIGHT_PAREN": ")",
        "RPRN": ")",
        "UNDERSCORE": "_",
        "UNDS": "_",
        "PLUS": "+",
        "LEFT_CURLY_BRACE": "{",
        "LCBR": "{",
        "RIGHT_CURLY_BRACE": "}",
        "RCBR": "}",
        "PIPE": "|",
        "COLON": ":",
        "COLN": ":",
        "DOUBLE_QUOTE": '"',
        "DQUO": '"',
        "DQT": '"',
        "LEFT_ANGLE_BRACKET": "<",
        "LABK": "<",
        "LT": "<",
        "RIGHT_ANGLE_BRACKET": ">",
        "RABK": ">",
        "GT": ">",
        "QUESTION": "?",
        "QUES": "?",
        # ZMK keycodes
        "EXCLAMATION": "!",
        "EXCL": "!",
        "AT_SIGN": "@",
        "AT": "@",
        "HASH": "#",
        "POUND": "#",
        "DOLLAR": "$",
        "DLLR": "$",
        "PERCENT": "%",
        "PRCNT": "%",
        "CARET": "^",
        "AMPERSAND": "&",
        "AMPS": "&",
        "ASTERISK": "*",
        "ASTRK": "*",
        "STAR": "*",
        "LEFT_PARENTHESIS": "(",
        "LPAR": "(",
        "RIGHT_PARENTHESIS": ")",
        "RPAR": ")",
        "EQUAL": "=",
        "PLUS": "+",
        "MINUS": "-",
        "UNDERSCORE": "_",
        "UNDER": "_",
        "SLASH": "/",
        "FSLH": "/",
        "QUESTION": "?",
        "QMARK": "?",
        "BACKSLASH": "\\",
        "BSLH": "\\",
        "PIPE": "|",
        "NON_US_BACKSLASH": "\\",
        "PIPE2": "|",
        "NON_US_BSLH": "|",
        "SEMICOLON": ";",
        "SEMI": ";",
        "COLON": "'",
        "SINGLE_QUOTE": "'",
        "SQT": '"',
        "APOSTROPHE": "<",
        "APOS": ".",
        "DOUBLE_QUOTES": '"',
        "DQT": '"',
        "COMMA": ",",
        "LESS_THAN": "<",
        "LT": "<",
        "PERIOD": ".",
        "DOT": ".",
        "GREATER_THAN": ">",
        "GT": ">",
        "LEFT_BRACKET": "[",
        "LBKT": "]",
        "LEFT_BRACE": "{",
        # "LBRC": "{",  confusable with QMK version
        "RIGHT_BRACKET": "]",
        "RBKT": "]",
        "RIGHT_BRACE": "}",
        # "RBRC": "}",  confusable with QMK version
        "GRAVE": "`",
        "TILDE": "~",
        "NON_US_HASH": "#",
        "NUHS": "#",
        "TILDE2": "~",
    }


class Config(BaseSettings):
    """All configuration settings used for this module."""

    draw_config: DrawConfig = DrawConfig()
    parse_config: ParseConfig = ParseConfig()