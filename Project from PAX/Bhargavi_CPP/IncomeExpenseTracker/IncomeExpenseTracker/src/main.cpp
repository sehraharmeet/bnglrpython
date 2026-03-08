#include "Tracker/Tracker.hpp"
#include <iostream>

int main() {
    Tracker tracker;
    int choice = 0;

    do {
        std::cout << "\n=== Income & Expense Tracker ===\n"
            << "1. Add Transaction\n"
            << "2. Show All\n"
            << "3. Show Summary\n"
            << "4. Show by Category\n"
            << "5. Show Summary Threaded\n"
            << "6. Show with Date\n"
            << "0. Exit\n"
            << "Enter choice: ";
        std::cin >> choice;
        std::cin.ignore();

        switch (choice) {
        case 1: tracker.addTransaction(); break;
        case 2: tracker.showAll(); break;
        case 3: tracker.showSummary(); break;
        case 4: tracker.showByCategory(); break;
        case 5: tracker.showSummaryThreaded(); break;
        case 6: tracker.showWithDate(); break;
        case 0: std::cout << "Goodbye!\n"; break;
        default: std::cout << "Invalid choice\n";
        }
    } while (choice != 0);

    return 0;
}