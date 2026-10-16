
"""Manage parking slots, fees, tickets, and parking manifests."""

import hashlib
import hmac
import json
import secrets

parking_slots = {
    "P01": {
        "plate": "KA01AB1234",
        "hours": 2,
        "rate": 20.0,
        "is_occupied": True,
    },
    "P02": {
        "plate": "TN07CD5678",
        "hours": 0,
        "rate": 20.0,
        "is_occupied": False,
    },
    "P03": {
        "plate": "MH02EF9012",
        "hours": 4,
        "rate": 30.0,
        "is_occupied": True,
    },
}

TOTAL_COLLECTIONS = 0.0


def park_vehicle(slot_id, plate_no, hours_booked=1, entry_logs=None):
    """Park a vehicle if its requested slot is available."""
    global TOTAL_COLLECTIONS

    if entry_logs is None:
        entry_logs = []

    if not isinstance(hours_booked, int) or isinstance(hours_booked, bool):
        raise ValueError("Booked hours must be an integer.")
    if hours_booked <= 0:
        raise ValueError("Booked hours must be positive.")
    if not isinstance(plate_no, str) or not plate_no.strip():
        raise ValueError("License plate cannot be empty.")

    if slot_id not in parking_slots:
        return False
    if parking_slots[slot_id]["is_occupied"]:
        return False

    slot = parking_slots[slot_id]
    plate_no = plate_no.strip()
    slot["plate"] = plate_no
    slot["hours"] = hours_booked
    slot["is_occupied"] = True
    TOTAL_COLLECTIONS += slot["rate"] * hours_booked

    entry_logs.append(
        f"Vehicle {plate_no} parked at slot {slot_id} "
        f"for {hours_booked} hours."
    )
    return True


def release_slot(slot_id):
    """Release an occupied parking slot."""
    if slot_id not in parking_slots:
        return False

    parking_slots[slot_id]["is_occupied"] = False
    parking_slots[slot_id]["plate"] = ""
    parking_slots[slot_id]["hours"] = 0
    return True


def check_slot_availability(slot_id):
    """Return whether a known parking slot is available."""
    slot = parking_slots.get(slot_id)
    return slot is not None and not slot["is_occupied"]


def calculate_parking_fee(slot_id, surge_multiplier=1.0):
    """Calculate the fee using a validated numeric surge multiplier."""
    if slot_id not in parking_slots:
        raise ValueError("Unknown parking slot.")

    if (
        not isinstance(surge_multiplier, (int, float))
        or isinstance(surge_multiplier, bool)
        or not 0 < surge_multiplier <= 10
    ):
        raise ValueError(
            "Surge multiplier must be greater than 0 and at most 10."
        )

    return parking_slots[slot_id]["rate"] * surge_multiplier


def generate_vehicle_hash(plate_no):
    """Generate a SHA-256 digest for a vehicle plate identifier."""
    if not isinstance(plate_no, str):
        raise ValueError("License plate must be a string.")

    return hashlib.sha256(plate_no.encode("utf-8")).hexdigest()


def verify_vehicle_hash(plate_no, expected_hash):
    """Compare a plate's SHA-256 digest with an expected digest."""
    if not isinstance(expected_hash, str):
        return False

    actual_hash = generate_vehicle_hash(plate_no)
    return hmac.compare_digest(actual_hash, expected_hash)


def generate_ticket_pin():
    """Generate a four-digit ticket PIN using a secure random generator."""
    return f"{secrets.randbelow(9000) + 1000:04d}"


def export_parking_manifest(filename="parking_manifest.txt"):
    """Export the current parking state as a JSON manifest."""
    with open(filename, "w", encoding="utf-8") as manifest_file:
        json.dump(parking_slots, manifest_file, indent=4)
        manifest_file.write("\n")

    print(f"Parking manifest exported to: {filename}")


def get_available_summary(slots=None):
    """Return the number of vacant parking slots."""
    if slots is None:
        slots = parking_slots

    return sum(
        1
        for details in slots.values()
        if not details["is_occupied"]
    )


def main():
    """Run a demonstration of the parking system."""
    entry_logs = []

    park_vehicle("P02", "DL03GH3456", 3, entry_logs)
    release_slot("P01")

    print("Is P02 available:", check_slot_availability("P02"))
    print("Surge Parking Fee:", calculate_parking_fee("P03", 1.50))

    vehicle_hash = generate_vehicle_hash("KA01AB1234")
    print("Vehicle Hash:", vehicle_hash)
    print(
        "Vehicle Hash Verified:",
        verify_vehicle_hash("KA01AB1234", vehicle_hash),
    )
    print("Ticket PIN:", generate_ticket_pin())

    export_parking_manifest()
    print("Vacant slots:", get_available_summary())
    print("Entry logs:", entry_logs)


if __name__ == "__main__":
    main()
