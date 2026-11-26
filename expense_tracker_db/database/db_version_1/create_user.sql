-- Create user if not exists
CREATE USER IF NOT EXISTS 'expense_tracker_user'@'localhost';

GRANT USAGE ON *.* TO `expense_tracker_user`@`localhost`;
GRANT SELECT, INSERT, UPDATE, DELETE ON `expense\_tracker`.*
   TO `expense_tracker_user`@`localhost`;