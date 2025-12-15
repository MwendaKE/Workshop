// Include core Qt classes we need for our app
#include <QApplication>   // Manages the GUI application loop
#include <QWidget>        // Base class for all UI windows
#include <QGridLayout>    // Layout manager to arrange widgets in a grid
#include <QPushButton>    // For creating clickable buttons
#include <QLineEdit>      // For creating the calculator display area
#include <QLabel>         // (Optional) For text labels — not used here but commonly used

// Include the scripting engine used to evaluate math expressions like "3+4*2"
// QScriptEngine is old. You can replace it with QJSEngine, which does the same job (it evaluates math/JavaScript expressions safely).
#include <QJSEngine>  // ✅ Use this instead of QScriptEngine

// Define our main Calculator class, which inherits from QWidget
// QWidget is the base class for all visual elements in Qt
class Calculator : public QWidget {
    Q_OBJECT // This macro is required for Qt's signal-slot system (connect mechanism)

public:
    // Constructor — sets up everything when the Calculator object is created
    Calculator(QWidget *parent = nullptr) : QWidget(parent) {

        // 1️⃣ Create a grid layout to arrange widgets neatly
        QGridLayout *layout = new QGridLayout(this);

        // 2️⃣ Create the display area (like a text box showing numbers)
        display = new QLineEdit(this);         // Create the line edit
        display->setReadOnly(true);            // Prevent manual typing
        display->setAlignment(Qt::AlignRight); // Align text to the right side (like real calculators)
        layout->addWidget(display, 0, 0, 1, 4); // Place it at row 0, col 0, spanning 1 row and 4 columns

        // 3️⃣ Create the calculator buttons
        // These are all the keys the calculator will have
        QStringList buttons = {"7","8","9","/",
                               "4","5","6","*",
                               "1","2","3","-",
                               "0",".","=","+"};

        // Variable to track which button we're adding
        int pos = 0;

        // 4️⃣ Loop through 4 rows and 4 columns to create all buttons
        for (int row = 1; row <= 4; ++row) {
            for (int col = 0; col < 4; ++col) {

                // Get the button label (text)
                QString text = buttons[pos++];

                // Create a new QPushButton with that label
                QPushButton *btn = new QPushButton(text, this);

                // Add the button to our grid layout
                layout->addWidget(btn, row, col);

                // 5️⃣ Connect each button to a click event (signal-slot system)
                // When a button is clicked, it will call onButtonClick(text)
                connect(btn, &QPushButton::clicked, this, [this, text]() {
                    onButtonClick(text);
                });
            }
        }

        // 6️⃣ Apply the layout and set window properties
        setLayout(layout);
        setWindowTitle("Simple Calculator"); // Set window title
        resize(250, 300);                    // Set window size
    }

private:
    // 📘 Member variables
    QLineEdit *display;    // The calculator's display (screen)
    QString currentText;   // Holds the current expression being typed (like "3+5*2")

    // 📘 Method: Called every time a button is clicked
    void onButtonClick(QString text) {
        // If the user pressed "=" — we evaluate the expression
        if (text == "=") {
            QJSEngine engine;  // Create an expression evaluator

            // ✅ Evaluate the math expression stored in currentText
            // .evaluate() runs the expression (e.g., "3+5*2")
            // .toNumber() converts the result to a double (number)
            QString result = QString::number(engine.evaluate(currentText).toNumber());

            // Show result on display
            display->setText(result);

            // Save the result as new current text (for chaining operations)
            currentText = result;
        } else {
            // If not "=", just append the pressed key to the expression
            currentText += text;
            display->setText(currentText);
        }
    }
};

// Include the Meta-Object Compiler file — required for Q_OBJECT macro
#include "main.moc"

// 📘 The main function — entry point of every C++ program
int main(int argc, char *argv[]) {
    QApplication app(argc, argv); // Create the main application (must always exist in Qt GUI)
    Calculator window;            // Create an instance of our Calculator window
    window.show();                // Show the window on screen
    return app.exec();            // Start the event loop (keeps app running until closed)
}

