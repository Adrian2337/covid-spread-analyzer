class NumberParser:

    @staticmethod
    def int_with_space(no: str) -> int:
        return int(no.replace(" ", ""))

    @staticmethod
    def int_with_modifier(test_no: str) -> int:
        number_str, modifier_str = test_no.split(" ")
        number = float(number_str.replace(",", "."))
        if modifier_str == "tys.":
            modifier = 1000
        else:
            modifier = 1000000
        return int(number * modifier)
