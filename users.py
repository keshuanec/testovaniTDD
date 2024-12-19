"""
Správa uživatelských účtů a volání externího API
Vytvořte třídu `User`, která má atributy `username` (uživatelské jméno) a `email`.
Vytvořte třídu `UserManager`, která umožňuje přidávat uživatele a odesílat ověřovací e-mail prostřednictvím externí služby.
Metoda `send_verification_email(user)` ve třídě `UserManager` by měla volat metodu `send_email(to, subject, body)`,
která simuluje volání externího API pro odesílání e-mailu.
Použijte **mock** objekty, abyste otestovali, zda metoda `send_verification_email` volá `send_email` s odpovídajícími parametry.


"""