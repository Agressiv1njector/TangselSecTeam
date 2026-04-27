#!/usr/bin/env python3
"""
IDN Homograph Attack Educator Tool v3
======================================
Demonstrasi serangan IDN Homograph — menunjukkan bagaimana domain FAKE
yang terlihat seperti domain REAL bisa mengarahkan ke TARGET berbeda.

⚠️  DISCLAIMER: HANYA untuk EDUKASI dan AWARENESS.

Usage:
    python homograph_edu.py --domain bca.co.id
    python homograph_edu.py --domain bca.co.id --target xxxxx.co.id
    python homograph_edu.py --domain google.com --target evil-site.com
"""

import argparse
import unicodedata
import sys
import io

# Fix Windows encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# ============================================================
# ACCURATE HOMOGLYPH DATABASE
# HANYA karakter yang secara visual IDENTIK
# ============================================================
HOMOGLYPHS = {
    'a': [('\u0430', 'Cyrillic')],    # а = a
    'c': [('\u0441', 'Cyrillic')],    # с = c
    'e': [('\u0435', 'Cyrillic')],    # е = e
    'h': [('\u04BB', 'Cyrillic')],    # һ = h
    'i': [('\u0456', 'Cyrillic')],    # і = i
    'j': [('\u0458', 'Cyrillic')],    # ј = j
    'k': [('\u043A', 'Cyrillic')],    # к ~ k
    'o': [('\u043E', 'Cyrillic')],    # о = o
    'p': [('\u0440', 'Cyrillic')],    # р = p
    's': [('\u0455', 'Cyrillic')],    # ѕ = s
    'x': [('\u0445', 'Cyrillic')],    # х = x
    'y': [('\u0443', 'Cyrillic')],    # у = y
}


def to_punycode(domain):
    try:
        parts = domain.split('.')
        result = []
        for part in parts:
            try:
                result.append(part.encode('idna').decode('ascii'))
            except (UnicodeError, UnicodeDecodeError):
                result.append('xn--' + part.encode('punycode').decode('ascii'))
        return '.'.join(result)
    except Exception:
        return domain


def generate_single_swaps(domain):
    variants = []
    for i, ch in enumerate(domain):
        if ch.lower() in HOMOGLYPHS:
            for repl, script in HOMOGLYPHS[ch.lower()]:
                fake = domain[:i] + repl + domain[i+1:]
                variants.append({
                    'fake': fake,
                    'punycode': to_punycode(fake),
                    'change': f"'{ch}' -> '{repl}' ({script} U+{ord(repl):04X})",
                })
    return variants


def generate_full_fake(domain):
    fake = ''
    changes = []
    for ch in domain:
        if ch.lower() in HOMOGLYPHS:
            repl, script = HOMOGLYPHS[ch.lower()][0]
            fake += repl
            changes.append(f"'{ch}'->'{repl}'")
        else:
            fake += ch
    return {'fake': fake, 'punycode': to_punycode(fake), 'changes': changes}


def main():
    parser = argparse.ArgumentParser(description='IDN Homograph Educator v3')
    parser.add_argument('--domain', '-d', default='bca.co.id',
                        help='Domain to impersonate (default: bca.co.id)')
    parser.add_argument('--target', '-t', default=None,
                        help='Target URL the fake domain redirects to')
    args = parser.parse_args()

    domain = args.domain
    target = args.target

    print()
    print("=" * 72)
    print("  IDN HOMOGRAPH ATTACK -- EDUCATION TOOL v3")
    print("  For AUTHORIZED security testing ONLY")
    print("=" * 72)
    print()

    # Show attack scenario
    if target:
        print(f"  ATTACK SCENARIO:")
        print(f"  {'=' * 66}")
        print(f"  Victim sees   : https://{domain}/login")
        print(f"  Actually goes : https://{target}")
        print(f"  {'=' * 66}")
        print()

    # Replaceable chars
    replaceable = sorted(set(ch for ch in domain if ch.lower() in HOMOGLYPHS))
    print(f"  Domain       : {domain}")
    print(f"  Replaceable  : {', '.join(replaceable) if replaceable else 'None'}")
    print()

    if not replaceable:
        print("  No homoglyph-compatible characters found.")
        return

    # Single swaps
    variants = generate_single_swaps(domain)
    print(f"  SINGLE CHARACTER SWAPS ({len(variants)} variants):")
    print(f"  {'-' * 66}")
    for i, v in enumerate(variants, 1):
        line = f"  {i}. {v['fake']:<25} Punycode: {v['punycode']}"
        if target:
            line += f"  --> {target}"
        print(line)
        print(f"     Changed: {v['change']}")
        print()

    # Full fake
    full = generate_full_fake(domain)
    print(f"  FULL REPLACEMENT:")
    print(f"  {'-' * 66}")
    print(f"  Original : {domain}")
    print(f"  Fake     : {full['fake']}")
    print(f"  Punycode : {full['punycode']}")
    print(f"  Changes  : {', '.join(full['changes'])}")
    print()

    # Visual comparison
    print(f"  {'=' * 66}")
    print(f"  VISUAL COMPARISON")
    print(f"  {'=' * 66}")
    print()
    print(f"  REAL : {domain}")
    print(f"  FAKE : {full['fake']}")
    print()
    print(f"  {'Pos':<5} {'REAL':<8} {'Code':<12} {'FAKE':<8} {'Code':<12} {'Match'}")
    print(f"  {'---':<5} {'----':<8} {'----':<12} {'----':<8} {'----':<12} {'-----'}")

    for i in range(max(len(domain), len(full['fake']))):
        r = domain[i] if i < len(domain) else ''
        f = full['fake'][i] if i < len(full['fake']) else ''
        rc = f"U+{ord(r):04X}" if r else "-"
        fc = f"U+{ord(f):04X}" if f else "-"
        match = "SAME" if r == f else "DIFF!"
        print(f"  {i:<5} '{r}'    {rc:<12} '{f}'    {fc:<12} {match}")

    print()
    print(f"  Punycode REAL : {to_punycode(domain)}")
    print(f"  Punycode FAKE : {full['punycode']}")

    # Attack flow with target
    if target:
        print()
        print(f"  {'=' * 66}")
        print(f"  ATTACK FLOW SIMULATION")
        print(f"  {'=' * 66}")
        print()
        print(f"  Step 1: Attacker registers homoglyph domain")
        print(f"          Domain : {full['fake']}")
        print(f"          Punycode: {full['punycode']}")
        print()
        print(f"  Step 2: Attacker points domain to target server")
        print(f"          {full['fake']} --> {target}")
        print()
        print(f"  Step 3: Attacker creates phishing page at:")
        print(f"          https://{full['fake']}/login")
        print(f"          (looks like https://{domain}/login)")
        print()
        print(f"  Step 4: Victim receives link:")
        for v in variants[:3]:
            print(f"          https://{v['fake']}/login")
        print()
        print(f"  Step 5: Victim clicks link thinking it's {domain}")
        print(f"          Browser shows: https://{full['fake']}/login")
        print(f"          Actually at  : {target}")
        print()
        print(f"  Step 6: Victim enters credentials")
        print(f"          Credentials sent to: {target}")
        print()

        # Summary table
        print(f"  {'=' * 66}")
        print(f"  PHISHING LINK SUMMARY")
        print(f"  {'=' * 66}")
        print(f"  {'Fake Link (looks real)':<40} {'Actual Target'}")
        print(f"  {'-' * 40} {'-' * 25}")
        for v in variants:
            print(f"  https://{v['fake']:<30} --> {target}")
        print(f"  https://{full['fake']:<30} --> {target}")

    print()
    print(f"  {'=' * 66}")
    print(f"  EDUCATIONAL NOTES")
    print(f"  {'=' * 66}")
    print(f"  - Modern browsers show Punycode (xn--...) for mixed-script")
    print(f"  - Email clients & mobile apps may NOT show Punycode!")
    print(f"  - Always check SSL certificate for domain verification")
    print(f"  - Use dnstwist to monitor: dnstwist --registered {domain}")
    print(f"  - Register homoglyph variants of your own domain")
    print(f"  - Setup DMARC/SPF/DKIM for email protection")
    print()
    print(f"  THIS TOOL IS FOR EDUCATION ONLY.")
    print(f"  Do NOT use for phishing or any illegal activity.")
    print(f"  {'=' * 66}")
    print()


if __name__ == '__main__':
    main()
