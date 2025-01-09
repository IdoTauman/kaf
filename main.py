import re
import argparse
import os

# Translation dictionary: Hebrew to C
hebrew_to_c = {
    # headers
    "קפסטנדרטי.ח": "stdio.h",
    "ספריהסטנדרטית.ח": "stdlib.h",
    # types
    "קבוע": "const",
    "מבנה": "struct",
    "חיובי": "unsigned",
    "סימן": "signed",
    "ריק": "void",
    "מספור": "enum",
    "צורסוג": "typedef",
    "נדיף": "volatile",
    "סטטי": "static",
    "אוטומטי": "auto",
    "איחוד": "union",
    "רשם": "register",
    "חיצוני": "extern",
    "ניתןלשינוי": "mutable",
    "שלם": "int",
    "תו": "char",
    "ארוך": "long",
    "קצר": "short",
    "מרחף": "float",
    "כפול": "double",
    "קובץ": "file",
    # main
    "ראשי": "main",
    # control flow
    "אם": "if",
    "אחרת": "else",
    "החלף": "switch",
    "מקרה": "case",
    "ברירתמחדל": "default",
    "עבור": "for",
    "כאשר": "while",
    "עשה": "do",
    "המשך": "continue",
    "שבור": "break",
    "החזר": "return",
    "לךל": "goto",
    # function specifiers
    "תוךשורה": "inline",
    "אסור": "restrict",
    # functions
    "גודלשל": "sizeof",
    "סוגשל": "typeof",
    "ישורשל": "alignof",
    "אלתחזיר": "noreturn",
    "הקצה": "malloc",
    "הקצהבלוקים": "calloc",
    "הקצהמחדש": "realloc",
    "שחרר": "free",
    "צא": "exit",
    "בטל": "abort",
    "תולמספר": "atoi",
    "תכלול": "include",
    "הגדר": "define",
    "פפתח": "fopen",
    "פרהפתח": "freopen",
    "פסגור": "fclose",
    "פנקה": "fflush",
    "פקרא": "fread",
    "פכתוב": "fwrite",
    "פהשגתו": "fgetc",
    "פהנחתו": "fputc",
    "פהשגמחרוזת": "fgets",
    "פהנחמחרוזת": "fputs",
    "השגתו": "getchar",
    "הנחתו": "putchar",
    "סרוקפ": "scanf",
    "הדפספ": "printf",
    # macros
    "סוף_קובץ": "EOF",
    "בלם_גודל": "BUFSIZ",
    "שם_קובץ_מקס": "FILENAME_MAX",
    "קסטנדרטי": "STDIN",
    "פסטנדרטי": "STDOUT",
    "שגיאהסטנדרטי": "STDERR",

}

def translate_to_c(code, translation_dict):
    """
    Translates Hebrew code to C, including keywords and identifiers.

    Args:
        code (str): The Hebrew code to translate.
        translation_dict (dict): The dictionary for Hebrew-to-C translation.

    Returns:
        str: Translated C code.
    """
    def replace_keyword(match):
        word = match.group(0)
        return translation_dict.get(word, word)

    # Match reserved keywords and identifiers
    pattern = r'\b(' + '|'.join(re.escape(key) for key in translation_dict.keys()) + r')\b'
    translated_code = re.sub(pattern, replace_keyword, code)

    return translated_code

def read_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def main(input, output):
    # Input: Hebrew code
    hebrew_code = read_from_file(input)

    # Translate Hebrew to C
    c_code = translate_to_c(hebrew_code, hebrew_to_c)
    with open(output, "w", encoding="utf-8") as file:
        file.write(c_code)
    
    # Compile
    os.system(f"gcc {output}")
    os.system("a.exe")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate כ code to C")
    parser.add_argument("input", help="Path to the .כ file")
    parser.add_argument("output", nargs="?", default="main.c", help="Path to output file (optional)")
    args = parser.parse_args()
    main(args.input, args.output)
