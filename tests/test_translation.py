import pytest
from translation import translate_text

def test_de_to_en_translation():
    text = "Hallo Welt"
    result = translate_text(text, src_lang="de", tgt_lang="en")
    assert isinstance(result, str)
    assert any(word in result.lower() for word in ["hello", "world"])

def test_fr_to_en_translation():
    text = "Bonjour le monde"
    result = translate_text(text, src_lang="fr", tgt_lang="en")
    assert isinstance(result, str)
    assert any(word in result.lower() for word in ["hello", "world"])
