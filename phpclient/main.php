<?php
include_once "./utils/Utility.php";
include_once "./service/impl/ServiceProxy.php";
include_once "./interface/impl/UserInterface.php";

$utility = Utility::getInstance("./resources/constants.json");
$service = new ServiceProxy($utility);

(new UserInterface($service))->showUi();