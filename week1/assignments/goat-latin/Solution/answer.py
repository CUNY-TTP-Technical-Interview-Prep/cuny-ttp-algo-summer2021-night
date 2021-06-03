def toGoatLatin(self, sentence: str) -> str:
        sp = sentence.split()
        vowel = {'a','e','i','o','u'}
        r = ""
        counter = 1
        for word in sp:
            current = word
            if current[0].lower() in vowel:
                current = current + "ma" + "a" * counter
            else:
                temp = current[0] + "ma" + "a" * counter
                current = current[1:] + temp
            counter+= 1
            r = r + current + " "
        r = r[:-1]
        return r