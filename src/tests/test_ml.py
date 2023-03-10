from main import model_deserializer


def test_model_deserializer():
    with open(f"./tests/others/dummy_model.pkl", "rb") as dummy_model:
        try:
            model_deserializer(dummy_model)
        except Exception as e:
            print(f"test_model_deserializer error:  {e}")
            return 0
