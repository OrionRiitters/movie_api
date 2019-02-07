function jsonToHTML(jsonData) {
    let left_div = document.querySelector('#left-column');
    let right_div = document.querySelector('#right-column');

    if (jsonData['Response'] == 'True') {
        let attrSwitch = false;

        for (attr in jsonData) {

            let newElement = document.createElement('p');
            newElement.className = 'info-bit';

            if (attr != 'Response' && attrSwitch == false) {
                newElement.innerHTML = `${attr}: ${jsonData[attr]}`;
                left_div.appendChild(newElement);
            } else if (attr != 'Response') {
                newElement.innerHTML = `${attr}: ${jsonData[attr]}`;
                right_div.appendChild(newElement);
            }
            attrSwitch = !attrSwitch;
        }
    }
}

