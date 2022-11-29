from console import HBNBCommand
import unittest
from unittest.mock import create_autospec, patch
import sys
from io import StringIO
import os
import pep8


class TestMyCLI(unittest.TestCase):

    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]

    def test_pep8(self):
        """ test pep8 """
        style = pep8.StyleGuide(quiet=True)
        file_console = "console.py"
        file_test_console = "tests/test_console.py"
        check = style.check_files([file_console, file_test_console])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")

    @classmethod
    def teardown(cls):
        """ final statement """
        try:
            os.remove("file.json")
        except:
            pass

    def setUp(self):
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create_session(self, server=None):
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_create(self):
        """Tesing `active` command"""
        cli = self.create_session()
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('create'))
        self.assertEqual('** class name missing **',
                         Output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('create hola'))
        self.assertEqual("** class doesn't exist **",
                         Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
            self.assertEqual(36, len(Output.getvalue().strip()))

    def test_show(self):
        cli = self.create_session()
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('show'))
        self.assertEqual('** class name missing **',
                         Output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('show hola'))
        self.assertEqual("** class doesn't exist **",
                         Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('show {}'.format(cls)))
            self.assertEqual("** instance id missing **",
                             Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('show {} 123456'.format(cls)))
            self.assertEqual("** no instance found **",
                             Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('show {} {}'.format(cls, ids)))
            self.assertTrue(ids in Output.getvalue().strip())
            self.assertTrue(cls in Output.getvalue().strip())
            self.assertTrue("created_at" in Output.getvalue().strip())
            self.assertTrue("updated_at" in Output.getvalue().strip())

        """ <class>.show(<id>) method """

        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.show()'.format(cls)))
            self.assertEqual("** instance id missing **",
                             Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.show("23456")'.format(cls)))
            self.assertEqual("** no instance found **",
                             Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.show("{}")'.format(cls, ids)))
            self.assertTrue(ids in Output.getvalue().strip())
            self.assertTrue(cls in Output.getvalue().strip())
            self.assertTrue("created_at" in Output.getvalue().strip())
            self.assertTrue("updated_at" in Output.getvalue().strip())

    def test_destroy(self):
        cli = self.create_session()
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('destroy'))
        self.assertEqual('** class name missing **',
                         Output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('destroy hola'))
        self.assertEqual("** class doesn't exist **",
                         Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('destroy {}'.format(cls)))
            self.assertEqual("** instance id missing **",
                             Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('destroy {} 123456'.format(cls)))
            self.assertEqual("** no instance found **",
                             Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('all'))
            self.assertTrue(ids in Output.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('destroy {} {}'.format(cls, ids)))
            self.assertFalse(ids in Output.getvalue().strip())
            self.assertEqual("", Output.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('all'))
            self.assertFalse(ids in Output.getvalue().strip())

        """ <class>.destroy(<id>) method """

        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.destroy()'.format(cls)))
            self.assertEqual("** instance id missing **",
                             Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.destroy("123456")'
                                 .format(cls)))
            self.assertEqual("** no instance found **",
                             Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('all'))
            self.assertTrue(ids in Output.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.destroy("{}")'
                                 .format(cls, ids)))
            self.assertFalse(ids in Output.getvalue().strip())
            self.assertEqual("", Output.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('all'))
            self.assertFalse(ids in Output.getvalue().strip())

    def test_all(self):
        cli = self.create_session()
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('all'))
        self.assertEqual('[', Output.getvalue().strip()[0])
        self.assertEqual(']', Output.getvalue().strip()[-1])
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('all hola'))
        self.assertEqual("** class doesn't exist **",
                         Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('all {}'.format(cls)))
                self.assertEqual('[', Output.getvalue().strip()[0])
                self.assertEqual(']', Output.getvalue().strip()[-1])
            self.assertTrue(ids in Output.getvalue().strip())

        """ <class>.all mode """

        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.all()'.format(cls)))
            self.assertEqual('[', Output.getvalue().strip()[0])
            self.assertEqual(']', Output.getvalue().strip()[-1])
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.all()'.format(cls)))
            self.assertTrue(ids in Output.getvalue().strip())

    def test_update(self):
        cli = self.create_session()
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('update'))
        self.assertEqual('** class name missing **',
                         Output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as Output:
            self.assertFalse(cli.onecmd('update hola'))
        self.assertEqual("** class doesn't exist **",
                         Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('update {}'.format(cls)))
            self.assertEqual("** instance id missing **",
                             Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('update {} 123456'.format(cls)))
            self.assertEqual("** no instance found **",
                             Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('update {} {}'.format(cls, ids)))
            self.assertEqual("** attribute name missing **",
                             Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('update {} {} attribute'
                                 .format(cls, ids)))
            self.assertEqual("** value missing **", Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('update {} {} attribute "test"'
                                 .format(cls, ids)))
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('show {} {}'.format(cls, ids)))
            self.assertTrue("attribute" in Output.getvalue().strip())
            self.assertTrue("test" in Output.getvalue().strip())

        """
        <class name>.update(<id>, <attribute name>, <attribute value>)
        method
        """

        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.update()'.format(cls)))
            self.assertEqual("** instance id missing **",
                             Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.update("123456")'.format(cls)))
            self.assertEqual("** no instance found **",
                             Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.update("{}")'
                                 .format(cls, ids)))
            self.assertEqual("** attribute name missing **",
                             Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.update("{}", "attribute")'
                                 .format(cls, ids)))
            self.assertEqual("** value missing **", Output.getvalue().strip())
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.update("{}", "attr", "test")'
                                 .format(cls, ids)))
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('show {} {}'.format(cls, ids)))
            self.assertTrue("attr" in Output.getvalue().strip())
            self.assertTrue("test" in Output.getvalue().strip())

        """ <class name>.update(<id>, <dictionary representation>) method """

        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
                ids = Output.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.update("{}", {{"num": 89}})'
                                 .format(cls, ids)))
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('show {} {}'.format(cls, ids)))
            self.assertTrue("num" in Output.getvalue().strip())
            self.assertTrue("89" in Output.getvalue().strip())

    def test_count(self):
        cli = self.create_session()
        for cls in TestMyCLI.classes:
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.count()'.format(cls)))
                number1 = int(Output.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('create {}'.format(cls)))
            with patch('sys.stdout', new=StringIO()) as Output:
                self.assertFalse(cli.onecmd('{}.count()'.format(cls)))
                number2 = int(Output.getvalue().strip())
            self.assertTrue(number2 == number1 + 1)

    def test_exit(self):
        """exit command"""
        cli = self.create_session()
        self.assertTrue(cli.onecmd("quit"))
