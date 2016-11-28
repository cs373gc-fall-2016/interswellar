var margin = {
    top: 10,
    right: 10,
    bottom: 10,
    left: 10
},
width = 840,
    height = 600;
var kx = function (d) {
    return d.x - 20;
};
var ky = function (d) {
    return d.y - 10;
};
//thie place the text x axis adjust this to center align the text
var tx = function (d) {
    return d.x - 3;
};
//thie place the text y axis adjust this to center align the text
var ty = function (d) {
    return d.y + 3;
};
//make an SVG
var svg = d3.select("#graph").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


//My JSON note the 
//no_parent: true this ensures that the node will not be linked to its parent
//hidden: true ensures that the nodes is not visible.
var root = {
    name: "",
    id: 1,
    hidden: true,
    children: [ {
            name: "Gaea",
            id: 16,
            no_parent: true,
            children: [{
            name: "Curetes & Dactyls",
            id: 12,

        }, {
            name: "Ourea",
            id: 13
        }, {
            name: "Pontus",
            id: 3,
            children: [{
                name: "Nereus",
                id: 741,
            }, {
                name: "Phorcys",
                id: 742,
            },{
                name: "Thaumas",
                id: 743,
            }]
        }, {
            name: "Silenus",
            id: 577
        }, {
            name: "",
            id: 4,
            hidden: true,
            no_parent: true,
            children: [{
                name: "Ananke",
                id: 5,
            }, {
                name: "Chronos Aeon",
                id: 6,
            }]
        }, {
            name: "Uranus",
            id: 11,
            children: [
            {
                name: "Phoebe",
                id: 708,
                no_parent: true
            },
            {
                        name: "",
                        id: 707,
                        no_parent: true,
                        hidden: true,
                        children: [{
                            name: "Leto",
                            id: 706,
                            children: [{
                                name: "Apollo",
                                id: 705
                            },{
                                name: "Artemis",
                                id: 704
                            }]
                        }]
            },
            {
                name: "Coeus",
                id: 709,
                no_parent: true
            },
            {
                name: "Philyra",
                id: 733,
                no_parent: true
            },{
                name: "",
                id: 716,
                hidden: true,
                no_parent: true,
                children: [{
                    name: "Ichthyocentaurs",
                    id: 714
                },{
                    name: "Chiron",
                    id: 715
                }]
            },{
                name: "Cronus",
                id: 741
            },{
                name: "",
                id: 713,
                hidden: true,
                no_parent: true,
                children: [{
                        name: "Dione",
                        id: 341,
                        no_parent: true
                    },
                    {
                        name: "",
                        id: 2,
                        no_parent: true,
                        hidden: true,
                        children: [{
                            name: "Aphrodite",
                            id: 340
                        }]
                    },
                     {
                        name: "Zeus",
                        id: 345
                    }, {
                        name: "Hera",
                        id: 342
                    }, {
                        name: "Hestia",
                        id: 343
                    
                    },{
                        name: "Poseidon",
                        id: 344
                    }, {
                        name: "Demeter",
                        id: 346
                    },{
                        name: "Hades",
                        id: 347
                    },{
                        name: "Hephaestus",
                        id: 348
                    },{
                        name: "Hebe",
                        id: 349
                    },{
                        name: "Ares",
                        id: 350
                    },{
                        name: "Eileithyia",
                        id: 351
                }]
            }, {
                name: "Rhea",
                id: 744,
            },
            {
                name: "Mnemosyne",
                id: 742,
            },{
                name: "Oceanus",
                id: 743,
            },{
                name: "Tethys",
                id: 745,
            },{
                name: "Themis",
                id: 746,
            }]
        }, {
            name: "Hydros",
            no_parent: true,
            id: 764,
            children: [{
                name: "Ananke",
                id: 787,
            }, {
                name: "Chronos Aeon",
                id: 782,
            }]
        },
            {
            name: "G",
            id: 7,
            children: [{
                name: "H",
                id: 8,
            }, {
                name: "I",
                id: 9,
            }]
        }]
        },{
        name: "",
        id: 2,
        no_parent: true,
        hidden: true,

    }, {
        name: "Psyche",
        id: 10,
        no_parent: true,
        children: [

        ]
    }, 
        {
        name: "Chaos",
        id: 725,
        no_parent: true,
        children: [{
                name: "Nyx",
                id: 794,
                children: [{
                    name: "Eris",
                    id: 739
                }, {
                    name: "Geras",
                    id: 795
                }, {
                    name: "Hypnos",
                    id: 796
                }, {
                    name: "Lyssa",
                    id: 797
                }, {
                    name: "Nemesis",
                    id: 798
                }, {
                    name: "Thanatos",
                    id: 799
                }]
            }]
    },
    ]
}
var allNodes = flatten(root);
//This maps the siblings together mapping uses the ID using the blue line
var siblings = [{
    source: {
        id: 3,
        name: "C"
    },
    target: {
        id: 11,
        name: "K"
    }
}, {
    source: {
        id: 12,
        name: "L"
    },
    target: {
        id: 13,
        name: "J"
    }
}, {
    source: {
        id: 5,
        name: "D"
    },
    target: {
        id: 6,
        name: "E"
    }
}, {
    source: {
        id: 16,
        name: "Q"
    },
    target: {
        id: 10,
        name: "M"
    }
}];

// Compute the layout.
var tree = d3.layout.tree().size([width, height]),
    nodes = tree.nodes(root),
    links = tree.links(nodes);

// Create the link lines.
svg.selectAll(".link")
    .data(links)
    .enter().append("path")
    .attr("class", "link")
    .attr("d", elbow);


var nodes = svg.selectAll(".node")
    .data(nodes)
    .enter();

//First draw sibling line with blue line
svg.selectAll(".sibling")
    .data(siblings)
    .enter().append("path")
    .attr("class", "sibling")
    .attr("d", sblingLine);

// Create the node rectangles.
nodes.append("rect")
    .attr("class", "node")
    .attr("height", 20)
    .attr("width", 40)
    .attr("id", function (d) {
    return d.id;
})
    .attr("display", function (d) {
    if (d.hidden) {
        return "none"
    } else {
        return ""
    };
})
    .attr("x", kx)
    .attr("y", ky);
// Create the node text label.
nodes.append("text")
    .text(function (d) {
    return d.name;
})
    .attr("x", tx)
    .attr("y", ty);


/**
This defines teh line between siblings.
**/
function sblingLine(d, i) {
    //start point
    var start = allNodes.filter(function (v) {
        if (d.source.id == v.id) {
            return true;
        } else {
            return false;
        }
    });
    //end point
    var end = allNodes.filter(function (v) {
        if (d.target.id == v.id) {
            return true;
        } else {
            return false;
        }
    });
    //define teh start coordinate and end co-ordinate
    var linedata = [{
        x: start[0].x,
        y: start[0].y
    }, {
        x: end[0].x,
        y: end[0].y
    }];
    var fun = d3.svg.line().x(function (d) {
        return d.x;
    }).y(function (d) {
        return d.y;
    }).interpolate("linear");
    return fun(linedata);
}

/*To make the nodes in flat mode.
This gets all teh nodes in same level*/
function flatten(root) {
    var n = [],
        i = 0;

    function recurse(node) {
        if (node.children) node.children.forEach(recurse);
        if (!node.id) node.id = ++i;
        n.push(node);
    }
    recurse(root);
    return n;
}
/** 
This draws the lines between nodes.
**/
function elbow(d, i) {
    if (d.target.no_parent) {
        return "M0,0L0,0";
    }
    var diff = d.source.y - d.target.y;
    //0.40 defines the point from where you need the line to break out change is as per your choice.
    var ny = d.target.y + diff * 0.40;

    linedata = [{
        x: d.target.x,
        y: d.target.y
    }, {
        x: d.target.x,
        y: ny
    }, {
        x: d.source.x,
        y: d.source.y
    }]

    var fun = d3.svg.line().x(function (d) {
        return d.x;
    }).y(function (d) {
        return d.y;
    }).interpolate("step-after");
    return fun(linedata);
}