export default Object.freeze({  
    comma: (value) => {
      var len, point, str;
  
      value = value + "";
      point = value.length % 3;
      len = value.length;
  
      str = value.substring(0, point);
      while (point < len) {
        if (str != "") str += ",";
        str += value.substring(point, point + 3);
        point += 3;
      }
  
      return str;
    },

    phone: (value) => {

        var str;

        str = value.substring(0, 3) + "-" + value.substring(3, 7) + "-" + value.substring(7, 11);

        return str;
    },

    acc: (value) => {
      value = value + "";
      var str;

      str = value.substring(0, 3) + "-" + value.substring(3, 5) + "-" + value.substring(5, 11) + "-" + value.substring(11, 12);

      return str;
  },
  });