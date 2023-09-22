#!/usr/bin/python3
"""The module defines a Base class for all other classes.
Its goal is to manage id attribute in all future classes.
"""
import json
import csv


class Base:
    """Base class.
    This class will be the "base" of all other classes in this project.
    It will manage id attribute for all the classes

    args:
         @id: The id for a specific instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate a new Base.

        arg:
            @id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list_dictionaries
        """
        # return json.dumps(list_dictionaries) if list_dictionaries else "[]"
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

        # if list_dictionaries is None:
        #    return "[]"

        # if not isinstance(list_dictionaries, list):
        #    raise TypeError("must be a list")

        # if not all(isinstance(item, dict) for item in list_dictionaries):
        #    raise TypeError("must be a list of dictionaries")

        # return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @staticmethod
    def from_json_string(json_string):
        """Return a list of JSON string representation.

        arg:
            json_string: a string representation of
                        a list of dictionaries
        """
        if json_string is None:
            return []

        if type(json_string) != str:
            raise TypeError("must be a string")

        return json.loads(json_string) if json_string else []

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes a JSON string representation
        of list_objs to a file.

        args:
            list_objs: list of instances who inherits from Base.
            Example (list of Rectangle, or list of Square) instances.
        """

        file_name = cls.__name__ + ".json"
        content = []

        if list_objs is not None:
            for idx, item in enumerate(list_objs):
                item = item.to_dictionary()
                dictionary = json.loads(cls.to_json_string(item))
                content.append(dictionary)

        with open(file_name, mode="w") as file_pointer:
            json.dump(content, file_pointer)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        arg:
            **dictionary: can be thought as a double
                          pointer to a dictionary
        """
        from models.rectangle import Rectangle
        from models.square import Square

        class_map = {
            "Rectangle": Rectangle,
            "Square": Square
        }
        if not dictionary:
            raise ValueError("Dictionary cannot be empty")

        if cls.__name__ not in class_map:
            raise ValueError("Invalid class name")

        num_of_attr = 2 if cls.__name__ == "Rectangle" else 1
        attr = [1] * num_of_attr
        new_instance = class_map[cls.__name__](*attr)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances.
         Returns:
            If file does not exist - an empty list
            otherwise - a  list of instances
        """
        file_name = cls.__name__ + ".json"
        instances = []

        try:
            with open(file_name,  mode="r", encoding="UTF8") as file_pointer:
                dict_content = cls.from_json_string(file_pointer.read())
                for dictionary in dict_content:
                    instance = cls.create(**dictionary)
                    instances.append(instance)
        except FileNotFoundError:
            pass

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize a CSV list of objects to a file

        args:
            list_objs(list): A list of inherited Base instances
        """
        filename = cls.__name__ + ".csv"

        with open(filename, mode="w", newline='', encoding="UTF8") as fp:

            writer = csv.writer(fp)

            for item in list_objs:
                item_dict = item.to_dictionary()

                if cls.__name__ == "Rectangle":
                    row = [item_dict["id"], item_dict["width"],
                           item_dict["height"],
                           item_dict["x"], item_dict["y"]]
                elif cls.__name__ == "Square":
                    row = [item_dict["id"], item_dict["size"],
                           item_dict["x"], item_dict["y"]]

                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize a csv file and return
        a list of classes instantiated from a CSV file

        # csv (comma-separated values)

        Returns:
                If the file exists - a list of classes instance
                otherwise - an empty list
        """

        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline="") as csvfile_pointer:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]

                reader = csv.DictReader(csvfile_pointer, fieldnames=fields)
                new_list_dicts = []
                for rd in reader:
                    new_dict = {}
                    for key, value in rd.items():
                        new_dict[key] = int(value)
                    new_list_dicts.append(new_dict)
                result = []
                for dict_obj in new_list_dicts:
                    result.append(cls.create(**dict_obj))
                return result

        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles
        and Squares using the turtle module.

        args:
             list_rectangles: A list of Rectangles to draw
             list_squares: A list of squares to draw
        """
        import turtle

        turtle.penup()
        turtle.pensize(10)
        turtle.bgcolor("cyan")
        turtle.color("white")
        turtle.hideturtle()
        turtle.goto(-250, 250)
        turtle.speed(0)

        def draw_shape(instance):
            """Draw a rectangle or square with specified
            dimensions and move the turtle's position.

            Args:
                 instance: An instance of Rectangle or Square
                 with width and height (or size).

            Description: This function draws the shape with the
            given dimensions, advances the turtle's position,
            and positions it for the next shape to be drawn.
            """

            turtle.pendown()
            for _ in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            move_by = instance.width + 50
            x_coordinate = round(turtle.xcor(), 5)
            turtle.goto(x_coordinate + move_by, turtle.ycor())

        for rect in list_rectangles:
            draw_shape(rect)

        turtle.goto(-250, 100)

        for sq in list_squares:
            draw_shape(sq)

        turtle.exitonclick()
