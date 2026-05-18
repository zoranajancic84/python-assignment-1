import subprocess

result = subprocess.run(
    ["python", "main.py"],
    input="Ana\n20\n",
    text=True,
    capture_output=True
)

output = result.stdout.strip()

expected = "Zdravo Ana, imaš 20 godina!"

if expected in output:
    print("PASS")
else:
    print("FAIL")
