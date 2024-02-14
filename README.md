# Table of contents 
- [What is NTRU?](#what-is-ntru)
- [Usage of this Python Module](#module-usage)
- [Docs](#other-docs)
	- [Algorithm](./Docs/NTRU%20Algorithm.md)
	- [Mathematical Requirements](./Docs/Required%20Mathematics%20for%20NTRU.md)
# What is NTRU?
[NTRU](https://en.wikipedia.org/wiki/NTRU) (N'th Degree Truncated Polynomial Ring Unit) is a Post Quantum Cryptographic System. Post-Quantum refers to the Cryptographic Encryption and Decryption that could be used after the widespread access to the Quantum computers become common.
## Need for a different (Post-Quantum) Cryptographic System.
The Current Cryptographic systems work on the NP-Hard problem of Factoring products of large Prime numbers, i.e. the difficulty and complexity of factorising the products of two large prime numbers is non-computable for a classical computer system.
#### Problem
These Classical Cryptographic systems can be broken using a quantum computer as the product of the large prime numbers can be factorised using [Shor's Algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm#:~:text=%22Shor's%20algorithm%22%20usually%20refers%20to,of%20the%20hidden%20subgroup%20problem.) on a Quantum Computer.
#### Solution
The solution is to come up with a different Cryptographic System which is based on either a different NP-Hard Problem or a completely different mathematical paradigm which maps the plain-text to the cipher-text in a manner which is not traceable.
# Module Usage
TBC
# Other Docs
- [NTRU Algorithm](./Docs/NTRU%20Algorithm.md)
	- Key-Generation
	- Encryption
	- Decryption