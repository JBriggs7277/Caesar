import webapp2
import cgi
from helpers import alphabet_position, rotate_character
from caesar import encrypt

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Caesar</title>
        <style type="text/css">
            .error {
                color = red;
            }

            form {
            background-color: blue;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px Arial;
            border-radius: 10px;
            }

            textarea {
            margin: 10px 0;
            width: 540px;
            height: 120px;
            }
        </style>
    </head>
    <body>
"""

page_footer = """
    </body>

</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):

        rot13_form = """
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text"></textarea>
            <br>
            <input type="submit">
        </form>
        """

        response = page_header + rot13_form + page_footer

        self.response.write(response)

    def post(self):

        text = self.request.get("text")
        rot13 = int(self.request.get("rot"))
        txt_esc = cgi.escape(text, quote= True)
        user_encrypt = encrypt(txt_esc, rot13)

        rot13_form = """
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">{0}</textarea>
            <input type="submit">
        </form>
        """.format(user_encrypt)

        response = page_header + rot13_form + page_footer

        self.response.write(response)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
