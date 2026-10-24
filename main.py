"""
Tangalar muammosi (LeetCode 518 - Coin Change II).

1, 2 va 5 so'mlik tangalar cheksiz miqdorda bor. 100 so'mni necha xil usulda yig'ish mumkin?
Tartib ahamiyatsiz: 5+2+1 va 1+2+5 bitta usul hisoblanadi.

Uchta mustaqil usul bilan yechiladi va natijalar solishtiriladi:
  1. Dinamik dasturlash (DP)
  2. Hosil qiluvchi funksiya: G(x) = 1 / ((1-x)(1-x^2)(1-x^5)) yoyilmasidagi x^N koeffitsienti
  3. Yopiq formula: sum_{k=0}^{N//5} (floor((N-5k)/2) + 1)
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

TANGALAR = (1, 2, 5)


def dp_usuli(n, tangalar=TANGALAR):
    """dp[s] - s so'mni yig'ish usullari soni. Har bir tanga navbat bilan qo'shiladi."""
    dp = [1] + [0] * n
    bosqichlar = []
    for t in tangalar:
        for s in range(t, n + 1):
            dp[s] += dp[s - t]
        bosqichlar.append((t, dp[n]))
    return dp[n], bosqichlar


def hosil_qiluvchi(n, tangalar=TANGALAR):
    """1/(1-x^t) = 1 + x^t + x^2t + ... qatorlarini ko'paytirib, x^n koeffitsientini oladi."""
    kopxad = [1] + [0] * n
    for t in tangalar:
        qator = [1 if i % t == 0 else 0 for i in range(n + 1)]
        yangi = [0] * (n + 1)
        for i, a in enumerate(kopxad):
            if a:
                for j in range(0, n + 1 - i, t):
                    yangi[i + j] += a * qator[j]
        kopxad = yangi
    return kopxad[n]


def yopiq_formula(n):
    """Faqat {1, 2, 5} uchun: k ta beshlik tanlansa, qolgan qismni 1 va 2 bilan (r//2 + 1) xil to'ldirish mumkin."""
    return sum((n - 5 * k) // 2 + 1 for k in range(n // 5 + 1))


def barcha_kombinatsiyalar(n):
    """(beshlik, ikkilik, birlik) uchliklari: 5a + 2b + c = n."""
    return [
        (a, b, n - 5 * a - 2 * b)
        for a in range(n // 5, -1, -1)
        for b in range((n - 5 * a) // 2, -1, -1)
    ]


def tahlil(n):
    print(f"\n{'=' * 72}")
    print(f"  {n} SO'MNI 1, 2, 5 SO'MLIK TANGALAR BILAN YIG'ISH")
    print(f"{'=' * 72}")

    dp_javob, bosqichlar = dp_usuli(n)
    gf_javob = hosil_qiluvchi(n)
    formula_javob = yopiq_formula(n)

    print("\n  1) Dinamik dasturlash bosqichlari:")
    ishlatilgan = []
    for t, qiymat in bosqichlar:
        ishlatilgan.append(str(t))
        print(f"     {{{', '.join(ishlatilgan)}}} tangalar bilan: {qiymat} usul")

    print(f"\n  2) Hosil qiluvchi funksiya:  G(x) = 1 / ((1-x)(1-x²)(1-x⁵))")
    print(f"     [x^{n}] G(x) = {gf_javob}")

    print(f"\n  3) Yopiq formula:  Σ_k (⌊({n}-5k)/2⌋ + 1),  k = 0..{n // 5}")
    print(f"     = {formula_javob}")

    mos = dp_javob == gf_javob == formula_javob
    print(f"\n  JAVOB: {dp_javob} xil usul   (uch usul {'mos keldi ✓' if mos else 'MOS EMAS'})")

    print(f"\n  Beshliklar soni bo'yicha taqsimot:")
    print(f"  {'beshlik':>7} | {'qoldiq':>6} | {'usullar':>7} | grafik")
    eng_kop = n // 2 + 1
    for k in range(n // 5 + 1):
        r = n - 5 * k
        usul = r // 2 + 1
        print(f"  {k:>7} | {r:>6} | {usul:>7} | {'█' * round(usul / eng_kop * 40)}")

    kombinatsiyalar = barcha_kombinatsiyalar(n)
    tangalar_soni = [a + b + c for a, b, c in kombinatsiyalar]
    print(f"\n  Eng kam tanga  : {min(tangalar_soni)} ta")
    print(f"  Eng ko'p tanga : {max(tangalar_soni)} ta")

    if input("\n  Barcha kombinatsiyalarni chiqaraymi? (h/y): ").strip().lower().startswith("h"):
        for i, (a, b, c) in enumerate(kombinatsiyalar, 1):
            print(f"  {i:>4}. 5×{a:<2} + 2×{b:<2} + 1×{c:<3} = {n}   ({a + b + c} ta tanga)")


def main():
    while True:
        kirish = input("\nSummani kiriting (masalan 100), 'q' - chiqish: ").strip().lstrip("﻿")
        if kirish.lower() in ("q", "quit", "exit"):
            break
        try:
            n = int(kirish)
        except ValueError:
            print("  Xato: butun son kiriting.")
            continue
        if n < 0:
            print("  Xato: summa manfiy bo'lishi mumkin emas.")
            continue
        tahlil(n)


if __name__ == "__main__":
    main()
