class RailFenceCipher:
    def __init__(self, rails):
        self.rails = rails

    def encrypt(self, plaintext):
        rails = [""] * self.rails
        rail = 0
        direction = 1

        for char in plaintext:
            rails[rail] += char
            rail += direction
            if rail == 0 or rail == self.rails - 1:
                direction *= -1

        return "".join(rails)