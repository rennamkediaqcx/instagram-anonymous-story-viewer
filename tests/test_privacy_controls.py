from src.core.privacy_controls import PrivacyControls, PrivacyPolicy

def test_privacy_controls_defaults():
    pc = PrivacyControls()
    assert pc.policy == PrivacyPolicy.INCOGNITO
    assert pc.persist_history is False
    assert pc.redact_logs is True
