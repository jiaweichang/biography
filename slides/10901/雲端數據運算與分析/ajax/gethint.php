<?php
	
	$a[] = "Anna";
	$a[] = "Annq";
	$a[] = "Brittany";
	$a[] = "Cinderella";

	$q = $_REQUEST["q"];
	$hint  = "";

	if($q !== "")
	{
		$q = strtolower($q);
		$len = strlen($q);

		foreach ($a as $name) {
			if(stristr($q, substr($name, 0, $len)))
			{
				if($hint === ""){
					$hint = $name;
				}
				else
				{
					$hint .= ", $name";
				}
			}
		}

	}

	echo $hint === "" ? "no suggestion" : $hint;
?>