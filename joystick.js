console.log("reached");
        // var mqtt=mqtt.client();
        var broker = 'wss://test.mosquitto.org:8081/mqtt';
        var client  =mqtt.connect(broker);

        client.on('connect', function () {
            console.log("connected");
            $('#connect').html("Connected to "+broker);
        });
        $("#joy3Div").mouseenter(function(){
            // console.log($('#joy3PosizioneX').val())
            // console.log($('#joy3PosizioneY').val())
            console.log("enter");
            console.log($('#joy3Direzione').val())
            console.log($('#joy3X').val())
            console.log($('#joy3Y').val())
            $direction=$('#joy3Direzione').val();
            if($direction=="N"){
                console.log("N");
                client.publish("mousemovement", "north");
            }else if($direction=="NW"){
                console.log("NW");
                client.publish("mousemovement", "northwest");
            }else if($direction=="SW"){
                console.log("SW");
                client.publish("mousemovement", "northeast");
            }else if($direction=="S"){
                console.log("S");
                client.publish("mousemovement", "south");
            }else if($direction=="SE"){
                console.log("SE");
                client.publish("mousemovement", "southeast");
            }else if($direction=="NE"){
                console.log("NE");
                client.publish("mousemovement", "northeast");
            }
            else if($direction=="E"){
                console.log("E");
                client.publish("mousemovement", "east");
            }else if($direction=="W"){
                console.log("NE");
                client.publish("mousemovement", "west");
            }
        })

        $("#joy3Div").mouseleave(function(){
            console.log("left");
            // console.log($('#joy3PosizioneX').val())
            // console.log($('#joy3PosizioneY').val())
            console.log($('#joy3Direzione').val())
            console.log($('#joy3X').val())
            console.log($('#joy3Y').val())
        })

        // var broker = 'wss://mqtt.eclipse.org:443/mqtt';
        // var client  = mqtt.connect(broker);
        