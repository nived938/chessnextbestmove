with open('assets/ncm_desktop-ae2de5e21cd6dbe64018b4c73ead07ac.js', 'r', encoding='utf-8') as f:
    code = f.read()

target = 'Ya.get("https://nextchessmove.com/api/v4/ping";'
replacement = 'Ya.get("https://nextchessmove.com/api/v4/ping");'

assert target in code, f"Target not found: {target}"
code = code.replace(target, replacement)

with open('assets/ncm_desktop-ae2de5e21cd6dbe64018b4c73ead07ac.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully fixed missing parenthesis!")

