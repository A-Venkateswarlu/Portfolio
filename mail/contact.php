<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = strip_tags(trim($_POST["name"]));
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $subject = strip_tags(trim($_POST["subject"]));
    $message = trim($_POST["message"]);

    // Your Email Address (Change this to your email)
    $to = "your-email@example.com";

    // Email Subject
    $email_subject = "New Contact Form Submission: $subject";

    // Email Content
    $email_body = "You have received a new message from your website contact form.\n\n".
                  "Name: $name\n".
                  "Email: $email\n\n".
                  "Message:\n$message\n";

    // Email Headers
    $headers = "From: $email\n";
    $headers .= "Reply-To: $email\n";

    // Send the Email
    if (mail($to, $email_subject, $email_body, $headers)) {
        http_response_code(200);
        echo "Success";
    } else {
        http_response_code(500);
        echo "Error";
    }
} else {
    http_response_code(403);
    echo "Access Forbidden";
}
?>
