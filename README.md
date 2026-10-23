# Biodiesel from used cooking oil

Process to convert used cooking oil into biodiesel, tested on a small engine.

## Provenance

Ashutosh reports having built the original project. Original portfolio details are preserved in `original-project.json`. The controller family was ESP32, Arduino UNO and, for some experiments, Raspberry Pi. Exact historic wiring is no longer available.

The `reconstruction/` source was newly written on 23 October 2026 to recreate and explain the project logic. It is not the recovered historical source. Pin maps are explicit new implementation choices, not claims about the lost wiring.

## Run the reconstruction

From this project folder:

```powershell
cd reconstruction
python model.py
python -m unittest -v
```

Python 3.10+; standard library only. Demo inputs are synthetic. Tests check the new logic, not historical results.

## Project documents

- [Bio](BIO.md)
- [Methodology](METHODOLOGY.md)
- [Source guide](CODE.md)
- [Evidence inventory](EVIDENCE.md)
- [Validation](VALIDATION.md)
- [References and offline resources](resources/README.md)

## Continuing this project

Record the actual components used in your new build, photograph its wiring, save raw measurements, and record the test conditions. Commit new results with their real date. Preserve recovered history separately from the reconstruction. No historical performance numbers have been generated.

See [the reconstruction architecture](ARCHITECTURE.md) for the implementation boundary.
