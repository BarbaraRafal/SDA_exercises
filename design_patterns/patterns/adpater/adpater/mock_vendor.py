from vendor_adapter import VendorAdapter
from vendor import Vendor


MOCKVENDOR = (
    VendorAdapter(Vendor("Fabryka czekolady", 34, 'Polna')),
    VendorAdapter(Vendor("Farma", 13, "Leśna")),
    VendorAdapter(Vendor("Świat cynamonu", 53, "Słoneczna")),
)
