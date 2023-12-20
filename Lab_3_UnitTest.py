import Lab_3_Pereverzev as app
import unittest as ut

class TestMyApp(ut.TestCase):

    def SetUp(self):
        self.app = app

    def test_now_time(self):
        self.assertTrue(0 < app.Time.now_time() < 235959)

    def test_show_time(self):
        self.assertEqual(len(app.Time.show_time(55)), 8)
        self.assertIn(":", app.Time.show_time(55))

    def test_push_note(self):
        self.assertIsNotNone(app.QueueFunc.push_note(app.Queue().order, "Hello world!"))

    def test_pop_note(self):
        self.assertEqual(
            app.QueueFunc.pop_note(app.QueueFunc.push_note(app.Queue().order, "Hello world!"))[1],
            "Hello world!"
        )
        self.assertFalse(app.QueueFunc.pop_note(app.Queue().order))

    @ut.expectedFailure
    def test_pop_note_exp_failure(self):
        self.assertEqual(
            app.QueueFunc.pop_note(app.Queue().order)[1],
            "Hello world!"
        )

    def test_emptify_notes(self):
        notes = app.Queue().order
        notes_empty = app.Queue().order
        for i in range (3):
            notes = app.QueueFunc.push_note(notes, "TestNote")
        self.assertEqual(app.QueueFunc.pop_note(app.QueueFunc.emptify_notes(notes)), 
                         app.QueueFunc.pop_note(notes_empty))

    def test_delete_notes(self):
        self.assertIsNone(app.QueueFunc.delete_notes(app.Queue().order))
        with self.assertRaises(ValueError):
            app.QueueFunc.delete_notes(None)

    def tearDown(self):
        pass

if __name__ == '__main__':

    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    ut.main(testRunner=runner)

    ut.main()