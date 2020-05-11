<?php

include_once "./service/IService.php";
include_once "./utils/Utility.php";

class ServiceProxy implements IService
{
    private $__constants;

    public function __construct($constants)
    {
        $this->__constants = $constants->getConstants();
    }

    public function getFilesByName($name)
    {
        return $this->sendJsonRpcRequest(
            $this->__constants[Constants::$apiFilesByName],
            $name
        );
    }

    public function getFilesByText($text)
    {
        return $this->sendJsonRpcRequest(
            $this->__constants[Constants::$apiFilesByText],
            $text
        );
    }

    public function getFilesByBinary($binary)
    {
        return $this->sendJsonRpcRequest(
            $this->__constants[Constants::$apiFilesByBinary],
            $binary
        );
    }

    public function getDuplicates()
    {
        return $this->sendJsonRpcRequest(
            $this->__constants[Constants::$apiFilesDuplicated]
        );
    }

    private function sendJsonRpcRequest($methodInfo, $paramValue = null)
    {
        //create the parameters array
        $arr = array();
        if (array_key_exists("parameterName", $methodInfo)) {
            $arr = array($methodInfo["parameterName"] => $paramValue);
        }

        //create data that will be send to server
        $payload = json_encode(
            array(
                "jsonrpc" => "2.0",
                "method" => $methodInfo["name"],
                "id" => rand(),
                "params" => $arr
            )
        );

        //init the cUrlObject
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $this->__constants[Constants::$serverAddress]);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));

        //make the call, and convert the result into associative array and get the result from the jrpc object
        return json_decode(curl_exec($ch), true)["result"];
    }

}
