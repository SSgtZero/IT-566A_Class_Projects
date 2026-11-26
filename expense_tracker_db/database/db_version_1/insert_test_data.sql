USE `expense_tracker`;

INSERT INTO `categories` (`name`) VALUES
  ('Food'), ('Gas'), ('Bills'), ('Entertainment');

INSERT INTO `expenses` (`expense_date`, `category_id`, `description`, `amount`)
VALUES
  ('2026-11-01', 1, 'Groceries', 84.37),
  ('2026-11-03', 2, 'Fill up', 45.10'),
  ('2026-11-05', 3, 'Phone bill', 65.00),
  ('2026-11-08', 1, 'Lunch', 12.50);