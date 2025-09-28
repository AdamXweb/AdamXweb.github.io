#!/usr/bin/env python3
# buddy_solver.py
# Reproduces the decrypt from the JS for the Buddy NPC CTF challenge.

import base64
import hashlib
from Crypto.Cipher import AES  # pip install pycryptodome
from typing import List

# ----------------------------
# Paste the blobs exactly as in the JS:
# ----------------------------

DATA_B64 = (
"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"
)

ENCRYPTED_FLAG_B64 = (
"lYLlXdDqUMRvPPrzUcCt4/cGgXVmZsHB1L5bg1Vrylnx8G2rvIxhrfIWuRx2KPC28TW1LlMqwchfbootLTNwnaW6jw=="
)

# ----------------------------
# Known solution choices (0-based mapping in original JS):
# Original mapping in early writeup: 0=Interesting,1=Right,2=Yeah,3=I see
# The sequence we found (0..3) is:
KNOWN_CHOICES = [1,0,1,1,3,0,2,3,3,2,2,0,2,1,3,2,1,1,2,0,2,3,1,1,3,3,3,0,0,3]
# ----------------------------

def load_data():
	data = base64.b64decode(DATA_B64)
	enc = base64.b64decode(ENCRYPTED_FLAG_B64)
	if len(data) % 30 != 0:
		raise ValueError("DATA length is not a multiple of 30!")
	groups = len(data) // 30 // 4  # should be 30 groups
	# Alternate calculation: there are 4 choices per group, and group size 30 bytes
	assert (len(data) // 30) % 4 == 0
	n_groups = (len(data) // 30) // 4
	print(f"Loaded DATA: total bytes={len(data)}, groups={n_groups}")
	# Build a structure: data_groups[g][choice] => bytes
	data_groups = []
	for g in range(n_groups):
		choices = []
		for c in range(4):
			start = 30 * (4 * g + c)
			choices.append(data[start:start+30])
		data_groups.append(choices)
	return data_groups, enc

def simulate_choices_and_check(data_groups: List[List[bytes]], choices: List[int]) -> bytes:
	"""
	Simulate the XOR accumulation described in handleYapResponse.
	Start with st = 30 zero bytes. For each group g, XOR the chosen 30-byte slice.
	Return the final st as bytes.
	"""
	if len(choices) != len(data_groups):
		raise ValueError("choices length mismatch")
	st = bytearray(30)
	for g, c in enumerate(choices):
		block = data_groups[g][c]
		for i in range(30):
			st[i] ^= block[i]
	return bytes(st)

def derive_key_from_choices(choices: List[int]) -> bytes:
	# JS uses choices.toString() which produces a comma-separated string with no spaces:
	# e.g. "1,0,1,..."
	s = ",".join(str(x) for x in choices)
	h = hashlib.sha256(s.encode()).digest()
	return h

def aesgcm_decrypt(key: bytes, ciphertext_and_tag: bytes) -> bytes:
	# From the JS: IV = 12 zero bytes; AES-GCM; ciphertext includes tag at end (16 bytes)
	iv = bytes([0]*12)
	if len(ciphertext_and_tag) < 16:
		raise ValueError("ciphertext too short")
	ct = ciphertext_and_tag[:-16]
	tag = ciphertext_and_tag[-16:]
	cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
	plaintext = cipher.decrypt_and_verify(ct, tag)
	return plaintext

def main():
	data_groups, enc = load_data()
	print("Simulating known choices...")
	final_st = simulate_choices_and_check(data_groups, KNOWN_CHOICES)
	if final_st == bytes([0xFF]*30):
		print("SUCCESS: final state is all 0xFF (condition satisfied).")
	else:
		print("FAIL: final state is not all 0xFF — here's the final state (hex):")
		print(final_st.hex())
		# still continue to try decrypt (may fail)
	key = derive_key_from_choices(KNOWN_CHOICES)
	print("Derived AES key (SHA-256 of choices string):", key.hex())
	try:
		plaintext = aesgcm_decrypt(key, enc)
		print("\n--- DECRYPTED FLAG ---")
		print(plaintext.decode())
		print("----------------------")
	except Exception as e:
		print("Decryption failed:", e)

if __name__ == "__main__":
	main()
