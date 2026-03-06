import unittest
from app import create_app, db
from app.models import Device, Department, Maintenance, QRCode

class DeviceModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_device_creation(self):
        device = Device(name='Ventilator', department=Department(name='ICU'))
        db.session.add(device)
        db.session.commit()
        self.assertEqual(device.name, 'Ventilator')

    def test_device_str(self):
        device = Device(name='Ventilator')
        self.assertEqual(str(device), 'Ventilator')

class DepartmentModelTestCase(unittest.TestCase):
    # Similar tests for Department model

class MaintenanceTrackingTestCase(unittest.TestCase):
    def test_maintenance_record(self):
        maintenance = Maintenance(device_id=1, date='2026-03-06', notes='General checkup')
        db.session.add(maintenance)
        db.session.commit()
        self.assertIsNotNone(maintenance)

class QRCodeGenerationTestCase(unittest.TestCase):
    def test_qr_code_generation(self):
        qr_code = QRCode.generate('Device 1')
        self.assertIsNotNone(qr_code)

if __name__ == '__main__':
    unittest.main()