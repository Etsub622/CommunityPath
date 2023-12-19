class ATM:
    def __init__(self):
        self.bank = defaultdict(int)
        self.totalnotes = {
            0: 20,
            1: 50,
            2: 100,
            3: 200,
            4: 500
        }

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.bank[self.totalnotes[i]] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        result = [0] * 5
        remaining = amount
        for i in range(4, -1, -1):
            note = self.totalnotes[i]
            count = min(remaining // note, self.bank[note])
            result[i] = count
            remaining -= count * note
        if remaining == 0:
            for i in range(5):
                self.bank[self.totalnotes[i]] -= result[i]
            return result
        else:
            return [-1]

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)