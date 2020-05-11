<?php

interface IService
{

    /**
     * This function is used in order to get all the files that
     *        have a name that contains @param $name
     * returns: a list of files
     */
    public function getFilesByName($name);

    /**
     * This function is used in order to get all the files that
     *        have a name that have in their content a text like @param $text
     * $text
     * returns: a list of files
     */
    public function getFilesByText($text);

    /**
     * This function is used in order to get all the files that
     *        have in their binary content a sequence o bytes from @param $binary
     * returns: a list of files
     */
    public function getFilesByBinary($binary);

    /**
     * This function is used in order to get all the files that
     *        have the content duplicated
     * returns: a list of files
     */
    public function getDuplicates();
}
