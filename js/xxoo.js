$(function () {
	console.log("clear plugthumb html and show loading");
	$(".index-list")
		.find(".plugthumb")
		.remove()
		.end()
		.find(".result")
		.removeClass("empty")
		.addClass("loading")
		.text("正在加载...")
		.show()
		;
	console.log("request json data");
	$.ajax({
		type:"get",
		url:"../data/images.json",
		async:true,
		dataType:"json",
		error: function(jqXHR, textStatus, errorThrown) {
			console.log("ajax request error, jqXHR=%s, textStatus=%s, errorThrown=%s", jqXHR, textStatus, errorThrown);
			$(".index-list")
				.find(".plugthumb")
				.remove()
				.end()
				.find(".result")
				.removeClass("loading")
				.addClass("empty")
				.text("对不起啦，没数据啊")
				.show()
				;
		},
		success: function(data, textStatus, jqXHR ) {
			console.log("ajax request success, data=%s, textStatus=%s", data, textStatus);
			console.log("clear old plugthumb html");
			$(".index-list .plugthumb").remove();
			console.log("data.length <= 0 is %s", data.length <= 0);
			if(data && data.length <= 0){
				console.log("request data is empty, show no data.");
				$(".index-list .result")
					.removeClass("loading")
					.addClass("empty")
					.text("对不起啦，没数据啊")
					.show()
					;
			} else {
				console.log("request data has item=%s, show data.", data.length);
				$(".index-list .result").hide();
				for (var i = 0; i < data.length; i++) {
					var node = $("#temp_plugthumb").clone();
					node.find("img.lazy")
						.attr("src", data[i].img)
						.attr("data-original", data[i].img)
						.attr("alt", data[i].title)
						.end()
						.find(".plug-title > a")
						.attr("href", data[i].href)
						.attr("title", data[i].title)
						.text(data[i].title)
						.end()
						.find(".plug-description")
						.remove()
						.end()
						.find(".plug-mesg .pull-right")
						.text(data[i].date)
						.end()
						;

					$(".index-list").append(node);
				}
			}
		}
	});

});
