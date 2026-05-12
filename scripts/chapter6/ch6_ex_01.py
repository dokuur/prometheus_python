text = "X-DSPAM-Confidence:    0.8475"

fnd = text.find('.')
print(float(text[fnd-1:]))
