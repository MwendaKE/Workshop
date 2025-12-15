#include <QApplication>
#include <QPushButton>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    QPushButton button("Hello Qt5 from VS Code!");
    button.resize(250, 70);
    button.show();
    return app.exec();
}
