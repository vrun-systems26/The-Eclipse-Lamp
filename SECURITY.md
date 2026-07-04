# Security Policy

## Supported Versions

This project is actively in development. Security fixes are applied to the most recent version on the `main` branch.

| Version | Supported          |
| ------- | ------------------ |
| main (latest) | :white_check_mark: |
| older commits | :x: |

## Reporting a Vulnerability

If you find a security issue — for example, a way to access the camera feed, notification system, or Pi remotely without authorization — please report it privately rather than opening a public issue.

**To report:**
- Open a [GitHub Security Advisory](../../security/advisories/new) on this repo (preferred), or
- Contact me directly at [varunchilukuri7@gmail.com]

Please include:
- A description of the vulnerability
- Steps to reproduce it
- What you think the potential impact is

**What to expect:**
- Acknowledgment within [a timeframe you're comfortable with, e.g. 5-7 days]
- I'll let you know if it's confirmed and roughly when a fix might land
- Credit in the changelog/README if you'd like it, once fixed

## Privacy & Responsible Use

This project involves a hidden camera and on-device AI person detection, which carries real privacy implications beyond typical software security. Please read this section before building or deploying it.

- **Intended use**: personal security monitoring in spaces you own or have explicit rights to monitor (e.g. your own home or office).
- **Not intended for**: monitoring shared/public spaces, spaces used by people who haven't consented, or any use that would violate local recording/surveillance laws. Laws on audio/video recording and consent vary significantly by location — check yours before deploying this anywhere other people are present.
- **Disclosure**: if you deploy this in any space shared with others (roommates, coworkers, guests), disclose that it's there. A hidden camera that's secretly hidden from the people it's recording, without their knowledge, is where this stops being a security project and starts being a real ethical and legal problem.
- **Data handling**: if you modify this project to store footage or detection logs, secure that data (encryption at rest, restricted access) and don't retain it longer than needed for its stated purpose.
- **No warranty on legality**: I'm not a lawyer, and this policy doesn't constitute legal advice — you're responsible for how and where you use this.

If you're contributing to this project and see a change that would make misuse easier (e.g. removing the disguise-detection cues, adding stealth-focused features beyond the original security-monitoring intent), please raise that as a concern in an issue or PR discussion rather than merging it silently.
