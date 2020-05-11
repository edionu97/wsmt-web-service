<?php

class Constants
{
    public static $serverAddress = "serverAddress";
    public static $apiFilesByName = "apiFilesByName";
    public static $apiFilesByText = "apiFilesByText";
    public static $apiFilesByBinary = "apiFilesByBinary";
    public static $apiFilesDuplicated = "apiFilesDuplicated";
}


class Utility
{

    private static $__instance = null;
    private $__constants;

    /**
     * Private constructor (is a singleton class)
     * @param $filename : the name of the file that contains the constants
     */
    private function __construct($filename)
    {
        $this->__constants = json_decode(file_get_contents($filename), true);
    }

    /**
     * This method is used in order to get an instance of the Utility class
     * @param $filename : the name of the constants file
     * @return null : singleton instance
     */
    public static function getInstance($filename)
    {

        if (Utility::$__instance == null) {
            Utility::$__instance = new Utility($filename);
        }

        return Utility::$__instance;
    }

    /**
     * Return the constants
     */
    public function getConstants()
    {
        return $this->__constants;
    }

}
