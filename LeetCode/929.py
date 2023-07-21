class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()

        for email in emails:
            splited = email.split("@")
            e = ""
            is_plus = False
            for c in splited[0]:
                if is_plus or c == ".":
                    continue
                elif c == "+":
                    is_plus = True
                    continue
                else:
                    e += c

            e += "@"
            e += splited[1]

            email_set.add(e)

        return len(email_set)
