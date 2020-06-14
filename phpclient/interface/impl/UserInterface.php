<?php

include_once "./interface/IUserInterface.php";
include_once "./service/IService.php";

class UserInterface implements IUserInterface
{
    private $__service;
    public function __construct(IService $service)
    {
        $this->__service = $service;
    }

    public function showUi()
    {
        $menu = $this->createMenu();
        while (true)
        {
            self::showOptions();

            echo "Enter option: ";$option = trim(fgets(STDIN));
            if(!array_key_exists($option, $menu)){
                echo "Wrong option";
                continue;
            }

            $menu[$option]();
        }
    }

    private static function showOptions(){
        echo "\n\n\n\n\n========================================\n\n";
        echo "     1. For getting the files filtered by name\n";
        echo "     2. For getting the files filtered by content\n";
        echo "     3. For getting the filed filtered by hex bytes\n";
        echo "     4. For getting all the duplicates\n";
        echo "     5. For existing the application\n";
        echo "\n========================================\n";
    }

    private function createMenu() {
        return array(
            "1" => function() {
                echo "Enter file name: "; $name = trim(fgets(STDIN));
                self::printArray($this->__service->getFilesByName($name));
            },
            "2" => function() {
                echo "Enter file text: "; $text = trim(fgets(STDIN));
                self::printArray($this->__service->getFilesByText($text));
            },
            "3" => function() {
                echo "Enter file bytes: "; $binary = explode(',', trim(fgets(STDIN)));
                self::printArray($this->__service->getFilesByBinary($binary));
            },
            "4" => function() {
                self::printArrayGroup($this->__service->getDuplicates());
            },
            "5" => function() {
                exit(0);
            }
        );
    }


    private static function printArrayGroup($resultGroup) {
        foreach ($resultGroup as $result) {
            echo "\n********\n";
            self::printArray($result);
            echo "********\n";
        }
    }

    private static function printArray($result) {

        if (count($result) == 0) {
            echo "No files are matching\n";
            return;
        }

        foreach ($result as $file) {
            echo $file."\n";
        }
    }

}
