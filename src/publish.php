<?php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;


$connection = new AMQPStreamConnection('rabbit', 5672, 'guest', 'guest');
$channel = $connection->channel();

$jsonParams = json_encode([
    'item1' => 1,
    'item2' => 2,
    'item3' => 3,
]);

$msg = new AMQPMessage(body: $jsonParams);
$channel->basic_publish(
    msg: $msg, 
    exchange: 'my_exchange', 
    routing_key: ''
);

$fh = fopen('php://stdout', 'w');
fwrite($fh, 'Hello World! Python'.PHP_EOL);
