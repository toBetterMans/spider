!function(t) {
    var e = {};
    function n(r) {
        if (e[r])
            return e[r].exports;
        var o = e[r] = {
            i: r,
            l: !1,
            exports: {}
        };
        return t[r].call(o.exports, o, o.exports, n),
        o.l = !0,
        o.exports
    }
    n.m = t,
    n.c = e,
    n.d = function(t, e, r) {
        n.o(t, e) || Object.defineProperty(t, e, {
            enumerable: !0,
            get: r
        })
    }
    ,
    n.r = function(t) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(t, "__esModule", {
            value: !0
        })
    }
    ,
    n.t = function(t, e) {
        if (1 & e && (t = n(t)),
        8 & e)
            return t;
        if (4 & e && "object" == typeof t && t && t.__esModule)
            return t;
        var r = Object.create(null);
        if (n.r(r),
        Object.defineProperty(r, "default", {
            enumerable: !0,
            value: t
        }),
        2 & e && "string" != typeof t)
            for (var o in t)
                n.d(r, o, function(e) {
                    return t[e]
                }
                .bind(null, o));
        return r
    }
    ,
    n.n = function(t) {
        var e = t && t.__esModule ? function() {
            return t.default
        }
        : function() {
            return t
        }
        ;
        return n.d(e, "a", e),
        e
    }
    ,
    n.o = function(t, e) {
        return Object.prototype.hasOwnProperty.call(t, e)
    }
    ,
    n.p = "",
    n(n.s = 269)
}([function(t, e) {
    var n = t.exports = {
        version: "2.5.7"
    };
    "number" == typeof __e && (__e = n)
}
, function(t, e) {
    var n = t.exports = "undefined" != typeof window && window.Math == Math ? window : "undefined" != typeof self && self.Math == Math ? self : Function("return this")();
    "number" == typeof __g && (__g = n)
}
, function(t, e, n) {
    "use strict";
    e.__esModule = !0,
    e.default = function(t, e) {
        if (!(t instanceof e))
            throw new TypeError("Cannot call a class as a function")
    }
}
, function(t, e, n) {
    var r = n(40)("wks")
      , o = n(26)
      , i = n(1).Symbol
      , a = "function" == typeof i;
    (t.exports = function(t) {
        return r[t] || (r[t] = a && i[t] || (a ? i : o)("Symbol." + t))
    }
    ).store = r
}
, function(t, e, n) {
    "use strict";
    e.__esModule = !0;
    var r = function(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }(n(75));
    e.default = function() {
        function t(t, e) {
            for (var n = 0; n < e.length; n++) {
                var o = e[n];
                o.enumerable = o.enumerable || !1,
                o.configurable = !0,
                "value"in o && (o.writable = !0),
                (0,
                r.default)(t, o.key, o)
            }
        }
        return function(e, n, r) {
            return n && t(e.prototype, n),
            r && t(e, r),
            e
        }
    }()
}
, , function(t, e, n) {
    var r = n(1)
      , o = n(0)
      , i = n(20)
      , a = n(15)
      , s = n(14)
      , u = function(t, e, n) {
        var c, l, f, h = t & u.F, d = t & u.G, p = t & u.S, v = t & u.P, g = t & u.B, y = t & u.W, m = d ? o : o[e] || (o[e] = {}), _ = m.prototype, w = d ? r : p ? r[e] : (r[e] || {}).prototype;
        for (c in d && (n = e),
        n)
            (l = !h && w && void 0 !== w[c]) && s(m, c) || (f = l ? w[c] : n[c],
            m[c] = d && "function" != typeof w[c] ? n[c] : g && l ? i(f, r) : y && w[c] == f ? function(t) {
                var e = function(e, n, r) {
                    if (this instanceof t) {
                        switch (arguments.length) {
                        case 0:
                            return new t;
                        case 1:
                            return new t(e);
                        case 2:
                            return new t(e,n)
                        }
                        return new t(e,n,r)
                    }
                    return t.apply(this, arguments)
                };
                return e.prototype = t.prototype,
                e
            }(f) : v && "function" == typeof f ? i(Function.call, f) : f,
            v && ((m.virtual || (m.virtual = {}))[c] = f,
            t & u.R && _ && !_[c] && a(_, c, f)))
    };
    u.F = 1,
    u.G = 2,
    u.S = 4,
    u.P = 8,
    u.B = 16,
    u.W = 32,
    u.U = 64,
    u.R = 128,
    t.exports = u
}
, function(t, e, n) {
    var r = n(13);
    t.exports = function(t) {
        if (!r(t))
            throw TypeError(t + " is not an object!");
        return t
    }
}
, function(t, e, n) {
    var r = n(7)
      , o = n(60)
      , i = n(42)
      , a = Object.defineProperty;
    e.f = n(9) ? Object.defineProperty : function(t, e, n) {
        if (r(t),
        e = i(e, !0),
        r(n),
        o)
            try {
                return a(t, e, n)
            } catch (t) {}
        if ("get"in n || "set"in n)
            throw TypeError("Accessors not supported!");
        return "value"in n && (t[e] = n.value),
        t
    }
}
, function(t, e, n) {
    t.exports = !n(21)(function() {
        return 7 != Object.defineProperty({}, "a", {
            get: function() {
                return 7
            }
        }).a
    })
}
, function(t, e, n) {
    "use strict";
    e.__esModule = !0;
    var r = function(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }(n(43));
    e.default = function(t, e) {
        if (!t)
            throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
        return !e || "object" !== (void 0 === e ? "undefined" : (0,
        r.default)(e)) && "function" != typeof e ? t : e
    }
}
, function(t, e, n) {
    "use strict";
    e.__esModule = !0;
    var r = a(n(107))
      , o = a(n(111))
      , i = a(n(43));
    function a(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    e.default = function(t, e) {
        if ("function" != typeof e && null !== e)
            throw new TypeError("Super expression must either be null or a function, not " + (void 0 === e ? "undefined" : (0,
            i.default)(e)));
        t.prototype = (0,
        o.default)(e && e.prototype, {
            constructor: {
                value: t,
                enumerable: !1,
                writable: !0,
                configurable: !0
            }
        }),
        e && (r.default ? (0,
        r.default)(t, e) : t.__proto__ = e)
    }
}
, function(t, e) {
    t.exports = React
}
, function(t, e) {
    t.exports = function(t) {
        return "object" == typeof t ? null !== t : "function" == typeof t
    }
}
, function(t, e) {
    var n = {}.hasOwnProperty;
    t.exports = function(t, e) {
        return n.call(t, e)
    }
}
, function(t, e, n) {
    var r = n(8)
      , o = n(25);
    t.exports = n(9) ? function(t, e, n) {
        return r.f(t, e, o(1, n))
    }
    : function(t, e, n) {
        return t[e] = n,
        t
    }
}
, function(t, e, n) {
    t.exports = {
        default: n(85),
        __esModule: !0
    }
}
, function(t, e, n) {
    var r = n(77)
      , o = n(38);
    t.exports = function(t) {
        return r(o(t))
    }
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = function(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }(n(43));
    function o(t, e) {
        return t.id && (t = t.id),
        e.id && (e = e.id),
        t < e ? t + ":" + e : e + ":" + t
    }
    function i(t) {
        return t
    }
    i.invert = function(t) {
        return t
    }
    ;
    function a(t, e, n) {
        (function(t, e, n) {
            return t.findIndex(function(t) {
                return t.id === e && t.type.findIndex(function(t) {
                    return t === n
                }) > -1
            }) > -1
        }
        )(t, e, n) || function(t, e, n) {
            var r = t.find(function(t) {
                return t.id === e
            });
            r || (r = {
                id: e,
                type: []
            },
            t.push(r)),
            r.type.push(n)
        }(t, e, n)
    }
    function s(t, e, n) {
        var r = n || 0;
        r = parseInt(2 * (r + 50));
        var o = t.x1
          , i = t.y1
          , a = t.x2
          , s = t.y2;
        if (t.w) {
            var u = t.w
              , c = t.h;
            a = t.x1 + u,
            s = t.y1 + c
        }
        var l = e.x
          , f = e.y;
        return l <= a + r && l >= o - r && f <= s + r && f >= i - r
    }
    var u = Array.prototype.forEach;
    function c(t, e, n) {
        if (t && e)
            if (t.forEach && t.forEach === u)
                t.forEach(e, n);
            else if (t.length === +t.length)
                for (var r = 0, o = t.length; r < o; r++)
                    e.call(n, t[r], r, t);
            else
                for (var i in t)
                    t.hasOwnProperty(i) && e.call(n, t[i], i, t)
    }
    function l(t, e) {
        var n = f(t, e);
        return -1 !== n ? t[n] : null
    }
    function f(t, e) {
        if (t && t.indexOf && "function" != typeof e)
            return t.indexOf(e);
        for (var n = 0, r = t.length; n < r; n++) {
            if (t[n] === e)
                return n;
            if ("function" == typeof e && e(t[n], n, t))
                return n
        }
        return -1
    }
    var h = function(t) {
        t.sort(function(t, e) {
            return t < e ? -1 : 1
        });
        for (var e = null, n = 0; n < t.length; n++)
            if (n !== t.length - 1) {
                var r = t[n + 1] - t[n];
                e || (e = r),
                r < e && (e = r)
            }
        return e
    };
    var d = {
        findInArr: l,
        indexOfArr: f,
        getQueryString: function(t) {
            var e = new RegExp("(^|&)" + t + "=([^&]*)(&|$)","i")
              , n = window.location.search.substr(1).match(e);
            return null != n ? decodeURIComponent(n[2]) : null
        },
        idSeq: o,
        defScaleLinear: i,
        lineSplit: function(t, e) {
            return 0 == e ? t : t <= e ? t : Math.pow(Math.pow(t, 2) - Math.pow(e, 2), .5)
        },
        angle: function(t, e) {
            var n = e.x - t.x
              , r = e.y - t.y
              , o = 360 * Math.atan(r / n) / (2 * Math.PI);
            if (n < 0 && r > 0)
                return 180 + o;
            if (n < 0 && r < 0)
                return 180 + o;
            if (n > 0 && r < 0)
                return 360 + o;
            if (0 === n) {
                if (r > 0)
                    return 90;
                if (r < 0)
                    return 270
            } else if (0 === r) {
                if (n > 0)
                    return 0;
                if (n < 0)
                    return 180
            }
            return o
        },
        lineCenter: function(t, e) {
            return {
                x: (t.x + e.x) / 2,
                y: (t.y + e.y) / 2
            }
        },
        lineLength: function(t, e) {
            return Math.pow(Math.pow(t.x - e.x, 2) + Math.pow(t.y - e.y, 2), .5)
        },
        angleXY: function(t, e, n, r) {
            var o = {
                y: Math.sin(2 * Math.PI / 360 * t) * e,
                x: Math.cos(2 * Math.PI / 360 * t) * e
            };
            return n && (r.x < n.x && (o.x = -o.x,
            o.y = -o.y),
            Math.pow(n.x - r.x, 2) + Math.pow(n.y - r.y, 2) < Math.pow(e, 2)) ? null : o
        },
        linkDates: function(t) {
            var e = [];
            t.forEach(function(t) {
                e.includes(t.properties.starttime) || e.push(parseInt(t.properties.starttime)),
                e.includes(t.properties.endtime) || e.push(parseInt(t.properties.endtime))
            }),
            e.sort(function(t, e) {
                return t < e ? -1 : 1
            }),
            -62135794739e3 === e[0] && e.splice(0, 1);
            var n = e[0]
              , r = e[e.length - 1];
            2533924224e5 === r && e.length > 2 && (r = e[e.length - 2]);
            for (var o = new Date(n).getFullYear(), i = [], a = new Date(r).getFullYear() + 1 - o + 1, s = 0; s < a; s++)
                i.push(s + o);
            return {
                timeDate: e,
                yearArr: i
            }
        },
        filterDateData: function(t, e, n, r) {
            var o = [];
            return e.forEach(function(t) {
                r ? t.properties.starttime <= n ? t.properties.starttime === n ? (a(o, t.startNode, "come"),
                a(o, t.endNode, "come"),
                t.dateType = "come") : t.properties.endtime > n ? (a(o, t.startNode, "normal"),
                a(o, t.endNode, "normal"),
                t.dateType = "normal") : t.properties.endtime === n ? (a(o, t.startNode, "leave"),
                a(o, t.endNode, "leave"),
                t.dateType = "leave") : t.properties.endtime < n ? (a(o, t.startNode, "prev"),
                a(o, t.endNode, "prev"),
                t.dateType = "prev") : console.log(t) : t.properties.starttime > n ? (a(o, t.startNode, "next"),
                a(o, t.endNode, "next"),
                t.dateType = "next") : console.log(t.properties) : t.properties.starttime < n ? (a(o, t.startNode, "normal"),
                a(o, t.endNode, "normal"),
                t.dateType = "normal") : t.properties.starttime === n ? (a(o, t.startNode, "come"),
                a(o, t.endNode, "come"),
                t.dateType = "come") : console.log(t)
            }),
            t.forEach(function(t) {
                t.dateType = function(t, e) {
                    var n = t.find(function(t) {
                        return String(t.id) === String(e)
                    });
                    return n ? n.type.includes("normal") ? "normal" : n.type.includes("leave") ? "leave" : n.type.includes("come") ? "come" : "none" : "none"
                }(o, t.id)
            }),
            function(t) {
                var e = [];
                return t.forEach(function(t) {
                    t.type.includes("leave") ? e.includes("leave") || e.push("leave") : t.type.includes("come") && (e.includes("come") || e.push("come"))
                }),
                e
            }(o)
        },
        elPlusOne: function(t, e) {
            return t[e = String(e)] = (t[e] || 0) + 1
        },
        findDataNode: function t(e, n, r, o) {
            var i = e[r];
            if (i) {
                var a = l(i, function(t) {
                    return t[n] == o && 1 == t.idPlus
                });
                return a || (c(i, function(e) {
                    var i = t(e, n, r, o);
                    i && (a = i)
                }),
                a)
            }
        },
        findOneDataNode: function t(e, n, r, o) {
            var i = e[r]
              , a = i.find(function(t) {
                return t[n] === o
            });
            return a || (c(i, function(e) {
                var i = t(e, n, r, o);
                i && (a = i)
            }),
            a)
        },
        findDataNodePlus: function t(e, n, r, o, i) {
            var a = e[r];
            if (a) {
                var s = l(a, function(t) {
                    return t[n] == o && t.uuid == i
                });
                return s || (c(a, function(e) {
                    var a = t(e, n, r, o, i);
                    a && (s = a)
                }),
                s)
            }
        },
        DeepLevelIds: function t(e, n, r, o) {
            var i = e[r]
              , a = [];
            return i.forEach(function(t) {
                t[o] && 0 === t[r].length && a.push(t[n])
            }),
            i.forEach(function(e) {
                var i = t(e, n, r, o);
                i.length > 0 && function(t, e) {
                    e.forEach(function(e) {
                        -1 === t.findIndex(function(t) {
                            return e == e
                        }) && t.push(e)
                    })
                }(a, i)
            }),
            a
        },
        LevelIds: function t(e, n, r, o, i) {
            var a = e[r]
              , s = []
              , u = !1;
            if (a.forEach(function(t) {
                i[t.id] > 0 && t.idPlus > 1 || (t[o] && 0 === t[r].length ? s.push(t[n]) : t[o] && (u = !0))
            }),
            s.length > 0)
                return s;
            if (u) {
                var c = {}
                  , l = c[r] = [];
                return a.for(function(t) {
                    t[r] && 1 === t.idPlus && function(t, e, n) {
                        e.forEach(function(e) {
                            -1 === t.findIndex(function(t) {
                                return n(t, e)
                            }) && t.push(e)
                        })
                    }(l, t[r], function(t, e) {
                        return t[n] == e[n]
                    })
                }),
                t(c, n, r, o, i)
            }
            return []
        },
        deepLevel: function t(e, n, r) {
            var o = 0;
            return e[r].forEach(function(e) {
                var i = t(e, n, r);
                o < i && (o = i)
            }),
            1 + o
        },
        poiSpaceMin: function(t) {
            var e = []
              , n = [];
            for (var r in t)
                if (t.hasOwnProperty(r)) {
                    var o = t[r];
                    e.push(o.x),
                    n.push(o.x)
                }
            return {
                x: h(e),
                y: h(n)
            }
        },
        deepCopy: function t(e, n) {
            n = n || {};
            for (var o in e)
                "object" === (0,
                r.default)(e[o]) && null !== e[o] ? (n[o] = e[o].constructor === Array ? [] : {},
                t(e[o], n[o])) : n[o] = e[o];
            return n
        },
        eachArr: c,
        uuid: function(t, e) {
            var n, r, o = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".split(""), i = [];
            if (e = e || o.length,
            t)
                for (n = 0; n < t; n++)
                    i[n] = o[0 | Math.random() * e];
            else
                for (i[8] = i[13] = i[18] = i[23] = "-",
                i[14] = "4",
                n = 0; n < 36; n++)
                    i[n] || (r = 0 | 16 * Math.random(),
                    i[n] = o[19 == n ? 3 & r | 8 : r]);
            return i.join("")
        },
        hitTest: s,
        hitTestLine: function(t, e, n, r) {
            r = r || 0;
            var o = t.x1
              , i = t.y1
              , a = t.x2
              , u = t.y2;
            if (t.w) {
                var c = t.w
                  , l = t.h;
                a = t.x1 + c,
                u = t.y1 + l
            }
            var f = e.x
              , h = e.y
              , d = n.x
              , p = (n.y - h) / (d - f)
              , v = (o - f) * p + h
              , g = (a - f) * p + h
              , y = Math.min(v, g)
              , m = Math.max(v, g)
              , _ = Math.min(i, u)
              , w = Math.max(i, u);
            return !!s(t, e, r) || !!s(t, n, r) || y >= _ - r && y <= w + r || m >= _ - r && m <= w + r || y <= _ + r && m >= _ - r || y <= w + r && m >= w - r
        },
        angle_sp_1: 2 * Math.PI / 360 * 1,
        isLinkedNode: function(t, e, n) {
            return t === n || !!e[o(t, n)]
        },
        dateFmt: function(t, e) {
            var n = new Date;
            e && (n = new Date(e)),
            t = t || "yyyy-MM-dd";
            var r = {
                "M+": n.getMonth() + 1,
                "d+": n.getDate(),
                "h+": n.getHours(),
                "m+": n.getMinutes(),
                "s+": n.getSeconds(),
                "q+": Math.floor((n.getMonth() + 3) / 3),
                S: n.getMilliseconds()
            };
            for (var o in /(y+)/.test(t) && (t = t.replace(RegExp.$1, (n.getFullYear() + "").substr(4 - RegExp.$1.length))),
            r)
                new RegExp("(" + o + ")").test(t) && (t = t.replace(RegExp.$1, 1 == RegExp.$1.length ? r[o] : ("00" + r[o]).substr(("" + r[o]).length)));
            return t
        },
        saveUrl: function(t, e, n) {
            var r = window
              , o = r.document;
            /constructor/i.test(r.HTMLElement) || r.safari,
            /CriOS\/[\d]+/.test(navigator.userAgent);
            var i = o.createElementNS("http://www.w3.org/1999/xhtml", "a");
            if ("download"in i)
                return i.href = t,
                i.download = e,
                void function(t) {
                    var e = new MouseEvent("click");
                    t.dispatchEvent(e)
                }(i);
            r.open(t, "_blank") || (r.location.href = t)
        },
        siteReduce: function(t) {
            var e = null;
            for (var n in t)
                if (t.hasOwnProperty(n)) {
                    var r = t[n];
                    if (r.sort(function(t, e) {
                        return t > e ? 1 : -1
                    }),
                    !(r.length < 2)) {
                        for (var o = null, i = 0; i < r.length - 1; i++) {
                            var a = r[i + 1] - r[i];
                            a <= 0 || (o || (o = a),
                            a < o && (o = a))
                        }
                        e || (e = o),
                        o < e && (e = o)
                    }
                }
            return e
        },
        poi5: function(t) {
            return t
        }
    };
    e.default = d
}
, function(t, e, n) {
    t.exports = {
        default: n(115),
        __esModule: !0
    }
}
, function(t, e, n) {
    var r = n(27);
    t.exports = function(t, e, n) {
        if (r(t),
        void 0 === e)
            return t;
        switch (n) {
        case 1:
            return function(n) {
                return t.call(e, n)
            }
            ;
        case 2:
            return function(n, r) {
                return t.call(e, n, r)
            }
            ;
        case 3:
            return function(n, r, o) {
                return t.call(e, n, r, o)
            }
        }
        return function() {
            return t.apply(e, arguments)
        }
    }
}
, function(t, e) {
    t.exports = function(t) {
        try {
            return !!t()
        } catch (t) {
            return !0
        }
    }
}
, function(t, e) {
    t.exports = {}
}
, function(t, e) {
    t.exports = !0
}
, function(t, e) {
    var n = {}.toString;
    t.exports = function(t) {
        return n.call(t).slice(8, -1)
    }
}
, function(t, e) {
    t.exports = function(t, e) {
        return {
            enumerable: !(1 & t),
            configurable: !(2 & t),
            writable: !(4 & t),
            value: e
        }
    }
}
, function(t, e) {
    var n = 0
      , r = Math.random();
    t.exports = function(t) {
        return "Symbol(".concat(void 0 === t ? "" : t, ")_", (++n + r).toString(36))
    }
}
, function(t, e) {
    t.exports = function(t) {
        if ("function" != typeof t)
            throw TypeError(t + " is not a function!");
        return t
    }
}
, function(t, e, n) {
    var r = n(63)
      , o = n(46);
    t.exports = Object.keys || function(t) {
        return r(t, o)
    }
}
, function(t, e, n) {
    var r = n(8).f
      , o = n(14)
      , i = n(3)("toStringTag");
    t.exports = function(t, e, n) {
        t && !o(t = n ? t : t.prototype, i) && r(t, i, {
            configurable: !0,
            value: e
        })
    }
}
, function(t, e) {
    t.exports = function(t) {
        var e = [];
        return e.toString = function() {
            return this.map(function(e) {
                var n = function(t, e) {
                    var n = t[1] || ""
                      , r = t[3];
                    if (!r)
                        return n;
                    if (e && "function" == typeof btoa) {
                        var o = function(t) {
                            return "/*# sourceMappingURL=data:application/json;charset=utf-8;base64," + btoa(unescape(encodeURIComponent(JSON.stringify(t)))) + " */"
                        }(r)
                          , i = r.sources.map(function(t) {
                            return "/*# sourceURL=" + r.sourceRoot + t + " */"
                        });
                        return [n].concat(i).concat([o]).join("\n")
                    }
                    return [n].join("\n")
                }(e, t);
                return e[2] ? "@media " + e[2] + "{" + n + "}" : n
            }).join("")
        }
        ,
        e.i = function(t, n) {
            "string" == typeof t && (t = [[null, t, ""]]);
            for (var r = {}, o = 0; o < this.length; o++) {
                var i = this[o][0];
                "number" == typeof i && (r[i] = !0)
            }
            for (o = 0; o < t.length; o++) {
                var a = t[o];
                "number" == typeof a[0] && r[a[0]] || (n && !a[2] ? a[2] = n : n && (a[2] = "(" + a[2] + ") and (" + n + ")"),
                e.push(a))
            }
        }
        ,
        e
    }
}
, function(t, e, n) {
    var r = {}
      , o = function(t) {
        var e;
        return function() {
            return void 0 === e && (e = t.apply(this, arguments)),
            e
        }
    }(function() {
        return window && document && document.all && !window.atob
    })
      , i = function(t) {
        var e = {};
        return function(t) {
            if ("function" == typeof t)
                return t();
            if (void 0 === e[t]) {
                var n = function(t) {
                    return document.querySelector(t)
                }
                .call(this, t);
                if (window.HTMLIFrameElement && n instanceof window.HTMLIFrameElement)
                    try {
                        n = n.contentDocument.head
                    } catch (t) {
                        n = null
                    }
                e[t] = n
            }
            return e[t]
        }
    }()
      , a = null
      , s = 0
      , u = []
      , c = n(127);
    function l(t, e) {
        for (var n = 0; n < t.length; n++) {
            var o = t[n]
              , i = r[o.id];
            if (i) {
                i.refs++;
                for (var a = 0; a < i.parts.length; a++)
                    i.parts[a](o.parts[a]);
                for (; a < o.parts.length; a++)
                    i.parts.push(g(o.parts[a], e))
            } else {
                var s = [];
                for (a = 0; a < o.parts.length; a++)
                    s.push(g(o.parts[a], e));
                r[o.id] = {
                    id: o.id,
                    refs: 1,
                    parts: s
                }
            }
        }
    }
    function f(t, e) {
        for (var n = [], r = {}, o = 0; o < t.length; o++) {
            var i = t[o]
              , a = e.base ? i[0] + e.base : i[0]
              , s = {
                css: i[1],
                media: i[2],
                sourceMap: i[3]
            };
            r[a] ? r[a].parts.push(s) : n.push(r[a] = {
                id: a,
                parts: [s]
            })
        }
        return n
    }
    function h(t, e) {
        var n = i(t.insertInto);
        if (!n)
            throw new Error("Couldn't find a style target. This probably means that the value for the 'insertInto' parameter is invalid.");
        var r = u[u.length - 1];
        if ("top" === t.insertAt)
            r ? r.nextSibling ? n.insertBefore(e, r.nextSibling) : n.appendChild(e) : n.insertBefore(e, n.firstChild),
            u.push(e);
        else if ("bottom" === t.insertAt)
            n.appendChild(e);
        else {
            if ("object" != typeof t.insertAt || !t.insertAt.before)
                throw new Error("[Style Loader]\n\n Invalid value for parameter 'insertAt' ('options.insertAt') found.\n Must be 'top', 'bottom', or Object.\n (https://github.com/webpack-contrib/style-loader#insertat)\n");
            var o = i(t.insertInto + " " + t.insertAt.before);
            n.insertBefore(e, o)
        }
    }
    function d(t) {
        if (null === t.parentNode)
            return !1;
        t.parentNode.removeChild(t);
        var e = u.indexOf(t);
        e >= 0 && u.splice(e, 1)
    }
    function p(t) {
        var e = document.createElement("style");
        return void 0 === t.attrs.type && (t.attrs.type = "text/css"),
        v(e, t.attrs),
        h(t, e),
        e
    }
    function v(t, e) {
        Object.keys(e).forEach(function(n) {
            t.setAttribute(n, e[n])
        })
    }
    function g(t, e) {
        var n, r, o, i;
        if (e.transform && t.css) {
            if (!(i = e.transform(t.css)))
                return function() {}
                ;
            t.css = i
        }
        if (e.singleton) {
            var u = s++;
            n = a || (a = p(e)),
            r = m.bind(null, n, u, !1),
            o = m.bind(null, n, u, !0)
        } else
            t.sourceMap && "function" == typeof URL && "function" == typeof URL.createObjectURL && "function" == typeof URL.revokeObjectURL && "function" == typeof Blob && "function" == typeof btoa ? (n = function(t) {
                var e = document.createElement("link");
                return void 0 === t.attrs.type && (t.attrs.type = "text/css"),
                t.attrs.rel = "stylesheet",
                v(e, t.attrs),
                h(t, e),
                e
            }(e),
            r = function(t, e, n) {
                var r = n.css
                  , o = n.sourceMap
                  , i = void 0 === e.convertToAbsoluteUrls && o;
                (e.convertToAbsoluteUrls || i) && (r = c(r));
                o && (r += "\n/*# sourceMappingURL=data:application/json;base64," + btoa(unescape(encodeURIComponent(JSON.stringify(o)))) + " */");
                var a = new Blob([r],{
                    type: "text/css"
                })
                  , s = t.href;
                t.href = URL.createObjectURL(a),
                s && URL.revokeObjectURL(s)
            }
            .bind(null, n, e),
            o = function() {
                d(n),
                n.href && URL.revokeObjectURL(n.href)
            }
            ) : (n = p(e),
            r = function(t, e) {
                var n = e.css
                  , r = e.media;
                r && t.setAttribute("media", r);
                if (t.styleSheet)
                    t.styleSheet.cssText = n;
                else {
                    for (; t.firstChild; )
                        t.removeChild(t.firstChild);
                    t.appendChild(document.createTextNode(n))
                }
            }
            .bind(null, n),
            o = function() {
                d(n)
            }
            );
        return r(t),
        function(e) {
            if (e) {
                if (e.css === t.css && e.media === t.media && e.sourceMap === t.sourceMap)
                    return;
                r(t = e)
            } else
                o()
        }
    }
    t.exports = function(t, e) {
        if ("undefined" != typeof DEBUG && DEBUG && "object" != typeof document)
            throw new Error("The style-loader cannot be used in a non-browser environment");
        (e = e || {}).attrs = "object" == typeof e.attrs ? e.attrs : {},
        e.singleton || "boolean" == typeof e.singleton || (e.singleton = o()),
        e.insertInto || (e.insertInto = "head"),
        e.insertAt || (e.insertAt = "bottom");
        var n = f(t, e);
        return l(n, e),
        function(t) {
            for (var o = [], i = 0; i < n.length; i++) {
                var a = n[i];
                (s = r[a.id]).refs--,
                o.push(s)
            }
            t && l(f(t, e), e);
            for (i = 0; i < o.length; i++) {
                var s;
                if (0 === (s = o[i]).refs) {
                    for (var u = 0; u < s.parts.length; u++)
                        s.parts[u]();
                    delete r[s.id]
                }
            }
        }
    }
    ;
    var y = function() {
        var t = [];
        return function(e, n) {
            return t[e] = n,
            t.filter(Boolean).join("\n")
        }
    }();
    function m(t, e, n, r) {
        var o = n ? "" : r.css;
        if (t.styleSheet)
            t.styleSheet.cssText = y(e, o);
        else {
            var i = document.createTextNode(o)
              , a = t.childNodes;
            a[e] && t.removeChild(a[e]),
            a.length ? t.insertBefore(i, a[e]) : t.appendChild(i)
        }
    }
}
, function(t, e, n) {
    t.exports = {
        default: n(84),
        __esModule: !0
    }
}
, function(t, e, n) {
    var r = n(38);
    t.exports = function(t) {
        return Object(r(t))
    }
}
, function(t, e) {
    e.f = {}.propertyIsEnumerable
}
, function(t, e) {
    t.exports = tycReducer
}
, function(t, e, n) {
    t.exports = {
        default: n(159),
        __esModule: !0
    }
}
, function(t, e) {
    t.exports = tycPaper
}
, function(t, e) {
    t.exports = function(t) {
        if (void 0 == t)
            throw TypeError("Can't call method on  " + t);
        return t
    }
}
, function(t, e, n) {
    var r = n(40)("keys")
      , o = n(26);
    t.exports = function(t) {
        return r[t] || (r[t] = o(t))
    }
}
, function(t, e, n) {
    var r = n(0)
      , o = n(1)
      , i = o["__core-js_shared__"] || (o["__core-js_shared__"] = {});
    (t.exports = function(t, e) {
        return i[t] || (i[t] = void 0 !== e ? e : {})
    }
    )("versions", []).push({
        version: r.version,
        mode: n(23) ? "pure" : "global",
        copyright: "© 2018 Denis Pushkarev (zloirock.ru)"
    })
}
, function(t, e, n) {
    var r = n(13)
      , o = n(1).document
      , i = r(o) && r(o.createElement);
    t.exports = function(t) {
        return i ? o.createElement(t) : {}
    }
}
, function(t, e, n) {
    var r = n(13);
    t.exports = function(t, e) {
        if (!r(t))
            return t;
        var n, o;
        if (e && "function" == typeof (n = t.toString) && !r(o = n.call(t)))
            return o;
        if ("function" == typeof (n = t.valueOf) && !r(o = n.call(t)))
            return o;
        if (!e && "function" == typeof (n = t.toString) && !r(o = n.call(t)))
            return o;
        throw TypeError("Can't convert object to primitive value")
    }
}
, function(t, e, n) {
    "use strict";
    e.__esModule = !0;
    var r = a(n(89))
      , o = a(n(98))
      , i = "function" == typeof o.default && "symbol" == typeof r.default ? function(t) {
        return typeof t
    }
    : function(t) {
        return t && "function" == typeof o.default && t.constructor === o.default && t !== o.default.prototype ? "symbol" : typeof t
    }
    ;
    function a(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    e.default = "function" == typeof o.default && "symbol" === i(r.default) ? function(t) {
        return void 0 === t ? "undefined" : i(t)
    }
    : function(t) {
        return t && "function" == typeof o.default && t.constructor === o.default && t !== o.default.prototype ? "symbol" : void 0 === t ? "undefined" : i(t)
    }
}
, function(t, e) {
    var n = Math.ceil
      , r = Math.floor;
    t.exports = function(t) {
        return isNaN(t = +t) ? 0 : (t > 0 ? r : n)(t)
    }
}
, function(t, e, n) {
    var r = n(7)
      , o = n(76)
      , i = n(46)
      , a = n(39)("IE_PROTO")
      , s = function() {}
      , u = function() {
        var t, e = n(41)("iframe"), r = i.length;
        for (e.style.display = "none",
        n(64).appendChild(e),
        e.src = "javascript:",
        (t = e.contentWindow.document).open(),
        t.write("<script>document.F=Object<\/script>"),
        t.close(),
        u = t.F; r--; )
            delete u.prototype[i[r]];
        return u()
    };
    t.exports = Object.create || function(t, e) {
        var n;
        return null !== t ? (s.prototype = r(t),
        n = new s,
        s.prototype = null,
        n[a] = t) : n = u(),
        void 0 === e ? n : o(n, e)
    }
}
, function(t, e) {
    t.exports = "constructor,hasOwnProperty,isPrototypeOf,propertyIsEnumerable,toLocaleString,toString,valueOf".split(",")
}
, function(t, e, n) {
    e.f = n(3)
}
, function(t, e, n) {
    var r = n(1)
      , o = n(0)
      , i = n(23)
      , a = n(47)
      , s = n(8).f;
    t.exports = function(t) {
        var e = o.Symbol || (o.Symbol = i ? {} : r.Symbol || {});
        "_" == t.charAt(0) || t in e || s(e, t, {
            value: a.f(t)
        })
    }
}
, function(t, e, n) {
    "use strict";
    var r = n(27);
    t.exports.f = function(t) {
        return new function(t) {
            var e, n;
            this.promise = new t(function(t, r) {
                if (void 0 !== e || void 0 !== n)
                    throw TypeError("Bad Promise constructor");
                e = t,
                n = r
            }
            ),
            this.resolve = r(e),
            this.reject = r(n)
        }
        (t)
    }
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    }),
    e.discover_createShortPathRelationsExcel = e.discover_getShortPathSvg = e.discover_getShortPathPng = e.discover_createHiddenRelationsExcel = e.discover_getHiddenSvg = e.discover_getHiddenPng = e.company_getCompanyDiscoverLayout = e.discover_addShortestPathRecord = e.discover_addHiddenRecord = e.downloadAppTreePng = e.downloadTreeSVG = e.downloadTreePng = e.downloadSVG = e.downloadPng = e.loadCompanyDetail = void 0;
    var r = s(n(128))
      , o = s(n(131))
      , i = s(n(19))
      , a = (e.loadCompanyDetail = function() {
        var t = (0,
        o.default)(r.default.mark(function t(e) {
            return r.default.wrap(function(t) {
                for (; ; )
                    switch (t.prev = t.next) {
                    case 0:
                        return t.next = 2,
                        u("/dis/companyDetail.json", {
                            id: e
                        });
                    case 2:
                        return t.abrupt("return", t.sent);
                    case 3:
                    case "end":
                        return t.stop()
                    }
            }, t, this)
        }));
        return function(e) {
            return t.apply(this, arguments)
        }
    }(),
    e.downloadPng = function() {
        var t = (0,
        o.default)(r.default.mark(function t(e) {
            return r.default.wrap(function(t) {
                for (; ; )
                    switch (t.prev = t.next) {
                    case 0:
                        return t.next = 2,
                        c("/dis/downloadPng.json", e);
                    case 2:
                        return t.abrupt("return", t.sent);
                    case 3:
                    case "end":
                        return t.stop()
                    }
            }, t, this)
        }));
        return function(e) {
            return t.apply(this, arguments)
        }
    }(),
    e.downloadSVG = function() {
        var t = (0,
        o.default)(r.default.mark(function t(e) {
            return r.default.wrap(function(t) {
                for (; ; )
                    switch (t.prev = t.next) {
                    case 0:
                        return t.next = 2,
                        c("/dis/downloadSvg.json", e);
                    case 2:
                        return t.abrupt("return", t.sent);
                    case 3:
                    case "end":
                        return t.stop()
                    }
            }, t, this)
        }));
        return function(e) {
            return t.apply(this, arguments)
        }
    }(),
    e.downloadTreePng = function() {
        var t = (0,
        o.default)(r.default.mark(function t(e) {
            return r.default.wrap(function(t) {
                for (; ; )
                    switch (t.prev = t.next) {
                    case 0:
                        return t.next = 2,
                        c("/dis/downloadTreePng.json", e);
                    case 2:
                        return t.abrupt("return", t.sent);
                    case 3:
                    case "end":
                        return t.stop()
                    }
            }, t, this)
        }));
        return function(e) {
            return t.apply(this, arguments)
        }
    }(),
    e.downloadTreeSVG = function() {
        var t = (0,
        o.default)(r.default.mark(function t(e) {
            return r.default.wrap(function(t) {
                for (; ; )
                    switch (t.prev = t.next) {
                    case 0:
                        return t.next = 2,
                        c("/dis/downloadTreeSvg.json", e);
                    case 2:
                        return t.abrupt("return", t.sent);
                    case 3:
                    case "end":
                        return t.stop()
                    }
            }, t, this)
        }));
        return function(e) {
            return t.apply(this, arguments)
        }
    }(),
    e.downloadAppTreePng = function() {
        var t = (0,
        o.default)(r.default.mark(function t(e) {
            return r.default.wrap(function(t) {
                for (; ; )
                    switch (t.prev = t.next) {
                    case 0:
                        return t.next = 2,
                        c("/dis/downloadAppTreePng.json", e);
                    case 2:
                        return t.abrupt("return", t.sent);
                    case 3:
                    case "end":
                        return t.stop()
                    }
            }, t, this)
        }));
        return function(e) {
            return t.apply(this, arguments)
        }
    }(),
    e.discover_addHiddenRecord = function() {
        var t = (0,
        o.default)(r.default.mark(function t(e) {
            return r.default.wrap(function(t) {
                for (; ; )
                    switch (t.prev = t.next) {
                    case 0:
                        return t.next = 2,
                        c("/cloud-std-me/discover/hidden/record.json", e);
                    case 2:
                        return t.abrupt("return", t.sent);
                    case 3:
                    case "end":
                        return t.stop()
                    }
            }, t, this)
        }));
        return function(e) {
            return t.apply(this, arguments)
        }
    }(),
    e.discover_addShortestPathRecord = function() {
        var t = (0,
        o.default)(r.default.mark(function t(e) {
            return r.default.wrap(function(t) {
                for (; ; )
                    switch (t.prev = t.next) {
                    case 0:
                        return t.next = 2,
                        c("/cloud-std-me/discover/shortest/record.json", e);
                    case 2:
                        return t.abrupt("return", t.sent);
                    case 3:
                    case "end":
                        return t.stop()
                    }
            }, t, this)
        }));
        return function(e) {
            return t.apply(this, arguments)
        }
    }(),
    e.company_getCompanyDiscoverLayout = function() {
        var t = (0,
        o.default)(r.default.mark(function t(e) {
            return r.default.wrap(function(t) {
                for (; ; )
                    switch (t.prev = t.next) {
                    case 0:
                        return t.next = 2,
                        u("/cloud-company/company/layout/discover/" + e + ".json");
                    case 2:
                        return t.abrupt("return", t.sent);
                    case 3:
                    case "end":
                        return t.stop()
                    }
            }, t, this)
        }));
        return function(e) {
            return t.apply(this, arguments)
        }
    }(),
    e.discover_getHiddenPng = function() {
        var t = (0,
        o.default)(r.default.mark(function t(e, n) {
            return r.default.wrap(function(t) {
                for (; ; )
                    switch (t.prev = t.next) {
                    case 0:
                        return t.next = 2,
                        c("/cloud-file/discover/hidden/" + e + "/png.json", n);
                    case 2:
                        return t.abrupt("return", t.sent);
                    case 3:
                    case "end":
                        return t.stop()
                    }
            }, t, this)
        }));
        return function(e, n) {
            return t.apply(this, arguments)
        }
    }(),
    e.discover_getHiddenSvg = function() {
        var t = (0,
        o.default)(r.default.mark(function t(e, n) {
            return r.default.wrap(function(t) {
                for (; ; )
                    switch (t.prev = t.next) {
                    case 0:
                        return t.next = 2,
                        c("/cloud-file/discover/hidden/" + e + "/svg.json", n);
                    case 2:
                        return t.abrupt("return", t.sent);
                    case 3:
                    case "end":
                        return t.stop()
                    }
            }, t, this)
        }));
        return function(e, n) {
            return t.apply(this, arguments)
        }
    }(),
    e.discover_createHiddenRelationsExcel = function() {
        var t = (0,
        o.default)(r.default.mark(function t(e) {
            return r.default.wrap(function(t) {
                for (; ; )
                    switch (t.prev = t.next) {
                    case 0:
                        return t.next = 2,
                        u("/cloud-file/discover/hidden/" + e + "/excelx.json");
                    case 2:
                        return t.abrupt("return", t.sent);
                    case 3:
                    case "end":
                        return t.stop()
                    }
            }, t, this)
        }));
        return function(e) {
            return t.apply(this, arguments)
        }
    }(),
    e.discover_getShortPathPng = function() {
        var t = (0,
        o.default)(r.default.mark(function t(e, n) {
            return r.default.wrap(function(t) {
                for (; ; )
                    switch (t.prev = t.next) {
                    case 0:
                        return t.next = 2,
                        c("/cloud-file/discover/shortest/" + e + "/png.json", n);
                    case 2:
                        return t.abrupt("return", t.sent);
                    case 3:
                    case "end":
                        return t.stop()
                    }
            }, t, this)
        }));
        return function(e, n) {
            return t.apply(this, arguments)
        }
    }(),
    e.discover_getShortPathSvg = function() {
        var t = (0,
        o.default)(r.default.mark(function t(e, n) {
            return r.default.wrap(function(t) {
                for (; ; )
                    switch (t.prev = t.next) {
                    case 0:
                        return t.next = 2,
                        c("/cloud-file/discover/shortest/" + e + "/svg.json", n);
                    case 2:
                        return t.abrupt("return", t.sent);
                    case 3:
                    case "end":
                        return t.stop()
                    }
            }, t, this)
        }));
        return function(e, n) {
            return t.apply(this, arguments)
        }
    }(),
    e.discover_createShortPathRelationsExcel = function() {
        var t = (0,
        o.default)(r.default.mark(function t(e) {
            return r.default.wrap(function(t) {
                for (; ; )
                    switch (t.prev = t.next) {
                    case 0:
                        return t.next = 2,
                        u("/cloud-file/discover/shortest/" + e + "/excelx.json");
                    case 2:
                        return t.abrupt("return", t.sent);
                    case 3:
                    case "end":
                        return t.stop()
                    }
            }, t, this)
        }));
        return function(e) {
            return t.apply(this, arguments)
        }
    }(),
    s(n(72)));
    function s(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    var u = function(t, e) {
        return new i.default(function(n, r) {
            a.default.get(t, {
                params: e
            }).then(function(t) {
                200 === t.status && n(t.data)
            }).catch(function(t) {
                r(t)
            })
        }
        )
    }
      , c = function(t, e, n) {
        return n = n || {},
        new i.default(function(r, o) {
            a.default.post(t, e, {
                headers: n
            }).then(function(t) {
                200 === t.status && r(t.data)
            }).catch(function(t) {
                o(t)
            })
        }
        )
    }
}
, function(t, e, n) {
    "use strict";
    var r = n(91)(!0);
    n(61)(String, "String", function(t) {
        this._t = String(t),
        this._i = 0
    }, function() {
        var t, e = this._t, n = this._i;
        return n >= e.length ? {
            value: void 0,
            done: !0
        } : (t = r(e, n),
        this._i += t.length,
        {
            value: t,
            done: !1
        })
    })
}
, function(t, e) {
    t.exports = tycD3
}
, function(t, e, n) {
    var r = n(44)
      , o = Math.min;
    t.exports = function(t) {
        return t > 0 ? o(r(t), 9007199254740991) : 0
    }
}
, function(t, e) {
    e.f = Object.getOwnPropertySymbols
}
, function(t, e, n) {
    n(95);
    for (var r = n(1), o = n(15), i = n(22), a = n(3)("toStringTag"), s = "CSSRuleList,CSSStyleDeclaration,CSSValueList,ClientRectList,DOMRectList,DOMStringList,DOMTokenList,DataTransferItemList,FileList,HTMLAllCollection,HTMLCollection,HTMLFormElement,HTMLSelectElement,MediaList,MimeTypeArray,NamedNodeMap,NodeList,PaintRequestList,Plugin,PluginArray,SVGLengthList,SVGNumberList,SVGPathSegList,SVGPointList,SVGStringList,SVGTransformList,SourceBufferList,StyleSheetList,TextTrackCueList,TextTrackList,TouchList".split(","), u = 0; u < s.length; u++) {
        var c = s[u]
          , l = r[c]
          , f = l && l.prototype;
        f && !f[a] && o(f, a, c),
        i[c] = i.Array
    }
}
, function(t, e, n) {
    var r = n(24)
      , o = n(3)("toStringTag")
      , i = "Arguments" == r(function() {
        return arguments
    }());
    t.exports = function(t) {
        var e, n, a;
        return void 0 === t ? "Undefined" : null === t ? "Null" : "string" == typeof (n = function(t, e) {
            try {
                return t[e]
            } catch (t) {}
        }(e = Object(t), o)) ? n : i ? r(e) : "Object" == (a = r(e)) && "function" == typeof e.callee ? "Arguments" : a
    }
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = s(n(2))
      , o = s(n(4))
      , i = s(n(19))
      , a = s(n(72));
    function s(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    a.default.interceptors.request.use(function(t) {
        return window._APP_AUTH && (window._APP_AUTH.token && (t.headers["X-AUTH-TOKEN"] = window._APP_AUTH.token),
        window._APP_AUTH.version && (t.headers.version = window._APP_AUTH.version),
        window._APP_AUTH.auth && (t.headers.Authorization = window._APP_AUTH.auth),
        window._APP_AUTH.channelID && (t.headers.channelID = window._APP_AUTH.channelID),
        window._APP_AUTH.deviceID && (t.headers.deviceID = window._APP_AUTH.deviceID)),
        t
    }, function(t) {
        return i.default.reject(t)
    });
    var u = function() {
        function t(e) {
            (0,
            r.default)(this, t),
            this.axios = a.default,
            (e = String(e || "/")).endsWith("/") || (e += "/"),
            this.host = e
        }
        return (0,
        o.default)(t, [{
            key: "fmtUrl",
            value: function(t) {
                return t.indexOf("://") > -1 ? t : (t.startsWith("/") && (t = t.substr(1)),
                "" + this.host + t)
            }
        }, {
            key: "getCloud",
            value: function(t, e, n) {
                var r = this.axios;
                return t = this.fmtUrl(t),
                e = e || {},
                n = n || {},
                new i.default(function(o, i) {
                    r.get(t, {
                        headers: n,
                        params: e,
                        withCredentials: !0
                    }).then(function(t) {
                        o(t.data)
                    }).catch(function(t) {
                        i(t)
                    })
                }
                )
            }
        }, {
            key: "get",
            value: function(t, e, n) {
                var r = this.axios;
                return t = this.fmtUrl(t),
                e = e || {},
                n = n || {},
                new i.default(function(o, i) {
                    r.get(t, {
                        headers: n,
                        params: e
                    }).then(function(t) {
                        if (t.data && t.data.special) {
                            var e = document.getElementsByTagName("head")[0]
                              , n = t.data.special.replace(".json", "")
                              , r = "https://cdn.tianyancha.com/fonts-styles/css/" + n + "/font.css"
                              , i = document.createElement("link");
                            i.setAttribute("rel", "stylesheet"),
                            i.href = r,
                            e.appendChild(i);
                            var a = document.body.className.split(" ");
                            a.push("font-" + n.split("/")[1]),
                            document.body.className = a.join(" ")
                        }
                        o(t.data)
                    }).catch(function(t) {
                        i(t)
                    })
                }
                )
            }
        }, {
            key: "postJSON",
            value: function(t, e) {
                var n = this.axios;
                return t = this.fmtUrl(t),
                e = e || {},
                new i.default(function(r, o) {
                    n({
                        method: "post",
                        url: t,
                        data: e,
                        withCredentials: !0
                    }).then(function(t) {
                        200 === t.status ? r(t.data) : o(t)
                    }).catch(function(t) {
                        o(t)
                    })
                }
                )
            }
        }, {
            key: "delMethod",
            value: function() {}
        }, {
            key: "objConcat",
            value: function(t) {
                return t
            }
        }, {
            key: "query_relation_company",
            value: function(t) {
                throw new ReferenceError("show implement query_relation_company")
            }
        }, {
            key: "query_relation_human",
            value: function(t, e) {
                throw new ReferenceError("show implement query_relation_human")
            }
        }, {
            key: "query_time_line",
            value: function(t) {
                throw new ReferenceError("show implement query_time_line")
            }
        }, {
            key: "query_equity_tree",
            value: function(t) {
                throw new ReferenceError("show implement query_time_line")
            }
        }, {
            key: "discover_getInvestRoot",
            value: function(t) {
                throw new ReferenceError("show implement discover_getInvestRoot")
            }
        }, {
            key: "discover_getInvest",
            value: function(t, e, n) {
                throw new ReferenceError("show implement discover_getInvest")
            }
        }, {
            key: "downloadPng",
            value: function(t) {
                return this.postJSON("/download/png.download", t)
            }
        }, {
            key: "discover_getHiddenRelations",
            value: function(t) {
                throw new ReferenceError("show implement discover_getHiddenRelations")
            }
        }, {
            key: "discover_getShortestPath",
            value: function(t) {
                throw new ReferenceError("show implement discover_getHiddenRelations")
            }
        }]),
        t
    }();
    e.default = u
}
, function(t, e) {
    t.exports = tycPolyfill
}
, function(t, e, n) {
    var r = n(14)
      , o = n(33)
      , i = n(39)("IE_PROTO")
      , a = Object.prototype;
    t.exports = Object.getPrototypeOf || function(t) {
        return t = o(t),
        r(t, i) ? t[i] : "function" == typeof t.constructor && t instanceof t.constructor ? t.constructor.prototype : t instanceof Object ? a : null
    }
}
, function(t, e, n) {
    t.exports = !n(9) && !n(21)(function() {
        return 7 != Object.defineProperty(n(41)("div"), "a", {
            get: function() {
                return 7
            }
        }).a
    })
}
, function(t, e, n) {
    "use strict";
    var r = n(23)
      , o = n(6)
      , i = n(62)
      , a = n(15)
      , s = n(22)
      , u = n(92)
      , c = n(29)
      , l = n(59)
      , f = n(3)("iterator")
      , h = !([].keys && "next"in [].keys())
      , d = function() {
        return this
    };
    t.exports = function(t, e, n, p, v, g, y) {
        u(n, e, p);
        var m, _, w, x = function(t) {
            if (!h && t in E)
                return E[t];
            switch (t) {
            case "keys":
            case "values":
                return function() {
                    return new n(this,t)
                }
            }
            return function() {
                return new n(this,t)
            }
        }, b = e + " Iterator", k = "values" == v, L = !1, E = t.prototype, S = E[f] || E["@@iterator"] || v && E[v], N = S || x(v), T = v ? k ? x("entries") : N : void 0, C = "Array" == e && E.entries || S;
        if (C && (w = l(C.call(new t))) !== Object.prototype && w.next && (c(w, b, !0),
        r || "function" == typeof w[f] || a(w, f, d)),
        k && S && "values" !== S.name && (L = !0,
        N = function() {
            return S.call(this)
        }
        ),
        r && !y || !h && !L && E[f] || a(E, f, N),
        s[e] = N,
        s[b] = d,
        v)
            if (m = {
                values: k ? N : x("values"),
                keys: g ? N : x("keys"),
                entries: T
            },
            y)
                for (_ in m)
                    _ in E || i(E, _, m[_]);
            else
                o(o.P + o.F * (h || L), e, m);
        return m
    }
}
, function(t, e, n) {
    t.exports = n(15)
}
, function(t, e, n) {
    var r = n(14)
      , o = n(17)
      , i = n(93)(!1)
      , a = n(39)("IE_PROTO");
    t.exports = function(t, e) {
        var n, s = o(t), u = 0, c = [];
        for (n in s)
            n != a && r(s, n) && c.push(n);
        for (; e.length > u; )
            r(s, n = e[u++]) && (~i(c, n) || c.push(n));
        return c
    }
}
, function(t, e, n) {
    var r = n(1).document;
    t.exports = r && r.documentElement
}
, function(t, e, n) {
    var r = n(63)
      , o = n(46).concat("length", "prototype");
    e.f = Object.getOwnPropertyNames || function(t) {
        return r(t, o)
    }
}
, function(t, e, n) {
    var r = n(34)
      , o = n(25)
      , i = n(17)
      , a = n(42)
      , s = n(14)
      , u = n(60)
      , c = Object.getOwnPropertyDescriptor;
    e.f = n(9) ? c : function(t, e) {
        if (t = i(t),
        e = a(e, !0),
        u)
            try {
                return c(t, e)
            } catch (t) {}
        if (s(t, e))
            return o(!r.f.call(t, e), t[e])
    }
}
, function(t, e) {}
, function(t, e, n) {
    var r = n(7)
      , o = n(27)
      , i = n(3)("species");
    t.exports = function(t, e) {
        var n, a = r(t).constructor;
        return void 0 === a || void 0 == (n = r(a)[i]) ? e : o(n)
    }
}
, function(t, e, n) {
    var r, o, i, a = n(20), s = n(119), u = n(64), c = n(41), l = n(1), f = l.process, h = l.setImmediate, d = l.clearImmediate, p = l.MessageChannel, v = l.Dispatch, g = 0, y = {}, m = function() {
        var t = +this;
        if (y.hasOwnProperty(t)) {
            var e = y[t];
            delete y[t],
            e()
        }
    }, _ = function(t) {
        m.call(t.data)
    };
    h && d || (h = function(t) {
        for (var e = [], n = 1; arguments.length > n; )
            e.push(arguments[n++]);
        return y[++g] = function() {
            s("function" == typeof t ? t : Function(t), e)
        }
        ,
        r(g),
        g
    }
    ,
    d = function(t) {
        delete y[t]
    }
    ,
    "process" == n(24)(f) ? r = function(t) {
        f.nextTick(a(m, t, 1))
    }
    : v && v.now ? r = function(t) {
        v.now(a(m, t, 1))
    }
    : p ? (i = (o = new p).port2,
    o.port1.onmessage = _,
    r = a(i.postMessage, i, 1)) : l.addEventListener && "function" == typeof postMessage && !l.importScripts ? (r = function(t) {
        l.postMessage(t + "", "*")
    }
    ,
    l.addEventListener("message", _, !1)) : r = "onreadystatechange"in c("script") ? function(t) {
        u.appendChild(c("script")).onreadystatechange = function() {
            u.removeChild(this),
            m.call(t)
        }
    }
    : function(t) {
        setTimeout(a(m, t, 1), 0)
    }
    ),
    t.exports = {
        set: h,
        clear: d
    }
}
, function(t, e) {
    t.exports = function(t) {
        try {
            return {
                e: !1,
                v: t()
            }
        } catch (t) {
            return {
                e: !0,
                v: t
            }
        }
    }
}
, function(t, e, n) {
    var r = n(7)
      , o = n(13)
      , i = n(49);
    t.exports = function(t, e) {
        if (r(t),
        o(e) && e.constructor === t)
            return e;
        var n = i.f(t);
        return (0,
        n.resolve)(e),
        n.promise
    }
}
, function(t, e) {
    t.exports = axios
}
, function(t, e, n) {
    var r = n(56)
      , o = n(3)("iterator")
      , i = n(22);
    t.exports = n(0).getIteratorMethod = function(t) {
        if (void 0 != t)
            return t[o] || t["@@iterator"] || i[r(t)]
    }
}
, function(t, e, n) {
    var r = n(6)
      , o = n(0)
      , i = n(21);
    t.exports = function(t, e) {
        var n = (o.Object || {})[t] || Object[t]
          , a = {};
        a[t] = e(n),
        r(r.S + r.F * i(function() {
            n(1)
        }), "Object", a)
    }
}
, function(t, e, n) {
    t.exports = {
        default: n(87),
        __esModule: !0
    }
}
, function(t, e, n) {
    var r = n(8)
      , o = n(7)
      , i = n(28);
    t.exports = n(9) ? Object.defineProperties : function(t, e) {
        o(t);
        for (var n, a = i(e), s = a.length, u = 0; s > u; )
            r.f(t, n = a[u++], e[n]);
        return t
    }
}
, function(t, e, n) {
    var r = n(24);
    t.exports = Object("z").propertyIsEnumerable(0) ? Object : function(t) {
        return "String" == r(t) ? t.split("") : Object(t)
    }
}
, function(t, e, n) {
    var r = n(7);
    t.exports = function(t, e, n, o) {
        try {
            return o ? e(r(n)[0], n[1]) : e(n)
        } catch (e) {
            var i = t.return;
            throw void 0 !== i && r(i.call(t)),
            e
        }
    }
}
, function(t, e, n) {
    var r = n(22)
      , o = n(3)("iterator")
      , i = Array.prototype;
    t.exports = function(t) {
        return void 0 !== t && (r.Array === t || i[o] === t)
    }
}
, function(t, e, n) {
    var r = n(3)("iterator")
      , o = !1;
    try {
        var i = [7][r]();
        i.return = function() {
            o = !0
        }
        ,
        Array.from(i, function() {
            throw 2
        })
    } catch (t) {}
    t.exports = function(t, e) {
        if (!e && !o)
            return !1;
        var n = !1;
        try {
            var i = [7]
              , a = i[r]();
            a.next = function() {
                return {
                    done: n = !0
                }
            }
            ,
            i[r] = function() {
                return a
            }
            ,
            t(i)
        } catch (t) {}
        return n
    }
}
, , , function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    e.default = {
        invalidCanvas: "无效的 canvas 选择器",
        undefinedCanvas: "未指定 canvas 选择器",
        invalidService: "无效的 service "
    }
}
, function(t, e, n) {
    var r = n(0)
      , o = r.JSON || (r.JSON = {
        stringify: JSON.stringify
    });
    t.exports = function(t) {
        return o.stringify.apply(o, arguments)
    }
}
, function(t, e, n) {
    n(86),
    t.exports = n(0).Object.getPrototypeOf
}
, function(t, e, n) {
    var r = n(33)
      , o = n(59);
    n(74)("getPrototypeOf", function() {
        return function(t) {
            return o(r(t))
        }
    })
}
, function(t, e, n) {
    n(88);
    var r = n(0).Object;
    t.exports = function(t, e, n) {
        return r.defineProperty(t, e, n)
    }
}
, function(t, e, n) {
    var r = n(6);
    r(r.S + r.F * !n(9), "Object", {
        defineProperty: n(8).f
    })
}
, function(t, e, n) {
    t.exports = {
        default: n(90),
        __esModule: !0
    }
}
, function(t, e, n) {
    n(51),
    n(55),
    t.exports = n(47).f("iterator")
}
, function(t, e, n) {
    var r = n(44)
      , o = n(38);
    t.exports = function(t) {
        return function(e, n) {
            var i, a, s = String(o(e)), u = r(n), c = s.length;
            return u < 0 || u >= c ? t ? "" : void 0 : (i = s.charCodeAt(u)) < 55296 || i > 56319 || u + 1 === c || (a = s.charCodeAt(u + 1)) < 56320 || a > 57343 ? t ? s.charAt(u) : i : t ? s.slice(u, u + 2) : a - 56320 + (i - 55296 << 10) + 65536
        }
    }
}
, function(t, e, n) {
    "use strict";
    var r = n(45)
      , o = n(25)
      , i = n(29)
      , a = {};
    n(15)(a, n(3)("iterator"), function() {
        return this
    }),
    t.exports = function(t, e, n) {
        t.prototype = r(a, {
            next: o(1, n)
        }),
        i(t, e + " Iterator")
    }
}
, function(t, e, n) {
    var r = n(17)
      , o = n(53)
      , i = n(94);
    t.exports = function(t) {
        return function(e, n, a) {
            var s, u = r(e), c = o(u.length), l = i(a, c);
            if (t && n != n) {
                for (; c > l; )
                    if ((s = u[l++]) != s)
                        return !0
            } else
                for (; c > l; l++)
                    if ((t || l in u) && u[l] === n)
                        return t || l || 0;
            return !t && -1
        }
    }
}
, function(t, e, n) {
    var r = n(44)
      , o = Math.max
      , i = Math.min;
    t.exports = function(t, e) {
        return (t = r(t)) < 0 ? o(t + e, 0) : i(t, e)
    }
}
, function(t, e, n) {
    "use strict";
    var r = n(96)
      , o = n(97)
      , i = n(22)
      , a = n(17);
    t.exports = n(61)(Array, "Array", function(t, e) {
        this._t = a(t),
        this._i = 0,
        this._k = e
    }, function() {
        var t = this._t
          , e = this._k
          , n = this._i++;
        return !t || n >= t.length ? (this._t = void 0,
        o(1)) : o(0, "keys" == e ? n : "values" == e ? t[n] : [n, t[n]])
    }, "values"),
    i.Arguments = i.Array,
    r("keys"),
    r("values"),
    r("entries")
}
, function(t, e) {
    t.exports = function() {}
}
, function(t, e) {
    t.exports = function(t, e) {
        return {
            value: e,
            done: !!t
        }
    }
}
, function(t, e, n) {
    t.exports = {
        default: n(99),
        __esModule: !0
    }
}
, function(t, e, n) {
    n(100),
    n(67),
    n(105),
    n(106),
    t.exports = n(0).Symbol
}
, function(t, e, n) {
    "use strict";
    var r = n(1)
      , o = n(14)
      , i = n(9)
      , a = n(6)
      , s = n(62)
      , u = n(101).KEY
      , c = n(21)
      , l = n(40)
      , f = n(29)
      , h = n(26)
      , d = n(3)
      , p = n(47)
      , v = n(48)
      , g = n(102)
      , y = n(103)
      , m = n(7)
      , _ = n(13)
      , w = n(17)
      , x = n(42)
      , b = n(25)
      , k = n(45)
      , L = n(104)
      , E = n(66)
      , S = n(8)
      , N = n(28)
      , T = E.f
      , C = S.f
      , M = L.f
      , I = r.Symbol
      , O = r.JSON
      , P = O && O.stringify
      , A = d("_hidden")
      , D = d("toPrimitive")
      , j = {}.propertyIsEnumerable
      , G = l("symbol-registry")
      , R = l("symbols")
      , z = l("op-symbols")
      , F = Object.prototype
      , q = "function" == typeof I
      , B = r.QObject
      , V = !B || !B.prototype || !B.prototype.findChild
      , Y = i && c(function() {
        return 7 != k(C({}, "a", {
            get: function() {
                return C(this, "a", {
                    value: 7
                }).a
            }
        })).a
    }) ? function(t, e, n) {
        var r = T(F, e);
        r && delete F[e],
        C(t, e, n),
        r && t !== F && C(F, e, r)
    }
    : C
      , H = function(t) {
        var e = R[t] = k(I.prototype);
        return e._k = t,
        e
    }
      , U = q && "symbol" == typeof I.iterator ? function(t) {
        return "symbol" == typeof t
    }
    : function(t) {
        return t instanceof I
    }
      , X = function(t, e, n) {
        return t === F && X(z, e, n),
        m(t),
        e = x(e, !0),
        m(n),
        o(R, e) ? (n.enumerable ? (o(t, A) && t[A][e] && (t[A][e] = !1),
        n = k(n, {
            enumerable: b(0, !1)
        })) : (o(t, A) || C(t, A, b(1, {})),
        t[A][e] = !0),
        Y(t, e, n)) : C(t, e, n)
    }
      , J = function(t, e) {
        m(t);
        for (var n, r = g(e = w(e)), o = 0, i = r.length; i > o; )
            X(t, n = r[o++], e[n]);
        return t
    }
      , W = function(t) {
        var e = j.call(this, t = x(t, !0));
        return !(this === F && o(R, t) && !o(z, t)) && (!(e || !o(this, t) || !o(R, t) || o(this, A) && this[A][t]) || e)
    }
      , K = function(t, e) {
        if (t = w(t),
        e = x(e, !0),
        t !== F || !o(R, e) || o(z, e)) {
            var n = T(t, e);
            return !n || !o(R, e) || o(t, A) && t[A][e] || (n.enumerable = !0),
            n
        }
    }
      , Z = function(t) {
        for (var e, n = M(w(t)), r = [], i = 0; n.length > i; )
            o(R, e = n[i++]) || e == A || e == u || r.push(e);
        return r
    }
      , Q = function(t) {
        for (var e, n = t === F, r = M(n ? z : w(t)), i = [], a = 0; r.length > a; )
            !o(R, e = r[a++]) || n && !o(F, e) || i.push(R[e]);
        return i
    };
    q || (s((I = function() {
        if (this instanceof I)
            throw TypeError("Symbol is not a constructor!");
        var t = h(arguments.length > 0 ? arguments[0] : void 0)
          , e = function(n) {
            this === F && e.call(z, n),
            o(this, A) && o(this[A], t) && (this[A][t] = !1),
            Y(this, t, b(1, n))
        };
        return i && V && Y(F, t, {
            configurable: !0,
            set: e
        }),
        H(t)
    }
    ).prototype, "toString", function() {
        return this._k
    }),
    E.f = K,
    S.f = X,
    n(65).f = L.f = Z,
    n(34).f = W,
    n(54).f = Q,
    i && !n(23) && s(F, "propertyIsEnumerable", W, !0),
    p.f = function(t) {
        return H(d(t))
    }
    ),
    a(a.G + a.W + a.F * !q, {
        Symbol: I
    });
    for (var $ = "hasInstance,isConcatSpreadable,iterator,match,replace,search,species,split,toPrimitive,toStringTag,unscopables".split(","), tt = 0; $.length > tt; )
        d($[tt++]);
    for (var et = N(d.store), nt = 0; et.length > nt; )
        v(et[nt++]);
    a(a.S + a.F * !q, "Symbol", {
        for: function(t) {
            return o(G, t += "") ? G[t] : G[t] = I(t)
        },
        keyFor: function(t) {
            if (!U(t))
                throw TypeError(t + " is not a symbol!");
            for (var e in G)
                if (G[e] === t)
                    return e
        },
        useSetter: function() {
            V = !0
        },
        useSimple: function() {
            V = !1
        }
    }),
    a(a.S + a.F * !q, "Object", {
        create: function(t, e) {
            return void 0 === e ? k(t) : J(k(t), e)
        },
        defineProperty: X,
        defineProperties: J,
        getOwnPropertyDescriptor: K,
        getOwnPropertyNames: Z,
        getOwnPropertySymbols: Q
    }),
    O && a(a.S + a.F * (!q || c(function() {
        var t = I();
        return "[null]" != P([t]) || "{}" != P({
            a: t
        }) || "{}" != P(Object(t))
    })), "JSON", {
        stringify: function(t) {
            for (var e, n, r = [t], o = 1; arguments.length > o; )
                r.push(arguments[o++]);
            if (n = e = r[1],
            (_(e) || void 0 !== t) && !U(t))
                return y(e) || (e = function(t, e) {
                    if ("function" == typeof n && (e = n.call(this, t, e)),
                    !U(e))
                        return e
                }
                ),
                r[1] = e,
                P.apply(O, r)
        }
    }),
    I.prototype[D] || n(15)(I.prototype, D, I.prototype.valueOf),
    f(I, "Symbol"),
    f(Math, "Math", !0),
    f(r.JSON, "JSON", !0)
}
, function(t, e, n) {
    var r = n(26)("meta")
      , o = n(13)
      , i = n(14)
      , a = n(8).f
      , s = 0
      , u = Object.isExtensible || function() {
        return !0
    }
      , c = !n(21)(function() {
        return u(Object.preventExtensions({}))
    })
      , l = function(t) {
        a(t, r, {
            value: {
                i: "O" + ++s,
                w: {}
            }
        })
    }
      , f = t.exports = {
        KEY: r,
        NEED: !1,
        fastKey: function(t, e) {
            if (!o(t))
                return "symbol" == typeof t ? t : ("string" == typeof t ? "S" : "P") + t;
            if (!i(t, r)) {
                if (!u(t))
                    return "F";
                if (!e)
                    return "E";
                l(t)
            }
            return t[r].i
        },
        getWeak: function(t, e) {
            if (!i(t, r)) {
                if (!u(t))
                    return !0;
                if (!e)
                    return !1;
                l(t)
            }
            return t[r].w
        },
        onFreeze: function(t) {
            return c && f.NEED && u(t) && !i(t, r) && l(t),
            t
        }
    }
}
, function(t, e, n) {
    var r = n(28)
      , o = n(54)
      , i = n(34);
    t.exports = function(t) {
        var e = r(t)
          , n = o.f;
        if (n)
            for (var a, s = n(t), u = i.f, c = 0; s.length > c; )
                u.call(t, a = s[c++]) && e.push(a);
        return e
    }
}
, function(t, e, n) {
    var r = n(24);
    t.exports = Array.isArray || function(t) {
        return "Array" == r(t)
    }
}
, function(t, e, n) {
    var r = n(17)
      , o = n(65).f
      , i = {}.toString
      , a = "object" == typeof window && window && Object.getOwnPropertyNames ? Object.getOwnPropertyNames(window) : [];
    t.exports.f = function(t) {
        return a && "[object Window]" == i.call(t) ? function(t) {
            try {
                return o(t)
            } catch (t) {
                return a.slice()
            }
        }(t) : o(r(t))
    }
}
, function(t, e, n) {
    n(48)("asyncIterator")
}
, function(t, e, n) {
    n(48)("observable")
}
, function(t, e, n) {
    t.exports = {
        default: n(108),
        __esModule: !0
    }
}
, function(t, e, n) {
    n(109),
    t.exports = n(0).Object.setPrototypeOf
}
, function(t, e, n) {
    var r = n(6);
    r(r.S, "Object", {
        setPrototypeOf: n(110).set
    })
}
, function(t, e, n) {
    var r = n(13)
      , o = n(7)
      , i = function(t, e) {
        if (o(t),
        !r(e) && null !== e)
            throw TypeError(e + ": can't set as prototype!")
    };
    t.exports = {
        set: Object.setPrototypeOf || ("__proto__"in {} ? function(t, e, r) {
            try {
                (r = n(20)(Function.call, n(66).f(Object.prototype, "__proto__").set, 2))(t, []),
                e = !(t instanceof Array)
            } catch (t) {
                e = !0
            }
            return function(t, n) {
                return i(t, n),
                e ? t.__proto__ = n : r(t, n),
                t
            }
        }({}, !1) : void 0),
        check: i
    }
}
, function(t, e, n) {
    t.exports = {
        default: n(112),
        __esModule: !0
    }
}
, function(t, e, n) {
    n(113);
    var r = n(0).Object;
    t.exports = function(t, e) {
        return r.create(t, e)
    }
}
, function(t, e, n) {
    var r = n(6);
    r(r.S, "Object", {
        create: n(45)
    })
}
, function(t, e) {
    t.exports = ReactDOM
}
, function(t, e, n) {
    n(67),
    n(51),
    n(55),
    n(116),
    n(124),
    n(125),
    t.exports = n(0).Promise
}
, function(t, e, n) {
    "use strict";
    var r, o, i, a, s = n(23), u = n(1), c = n(20), l = n(56), f = n(6), h = n(13), d = n(27), p = n(117), v = n(118), g = n(68), y = n(69).set, m = n(120)(), _ = n(49), w = n(70), x = n(121), b = n(71), k = u.TypeError, L = u.process, E = L && L.versions, S = E && E.v8 || "", N = u.Promise, T = "process" == l(L), C = function() {}, M = o = _.f, I = !!function() {
        try {
            var t = N.resolve(1)
              , e = (t.constructor = {})[n(3)("species")] = function(t) {
                t(C, C)
            }
            ;
            return (T || "function" == typeof PromiseRejectionEvent) && t.then(C)instanceof e && 0 !== S.indexOf("6.6") && -1 === x.indexOf("Chrome/66")
        } catch (t) {}
    }(), O = function(t) {
        var e;
        return !(!h(t) || "function" != typeof (e = t.then)) && e
    }, P = function(t, e) {
        if (!t._n) {
            t._n = !0;
            var n = t._c;
            m(function() {
                for (var r = t._v, o = 1 == t._s, i = 0, a = function(e) {
                    var n, i, a, s = o ? e.ok : e.fail, u = e.resolve, c = e.reject, l = e.domain;
                    try {
                        s ? (o || (2 == t._h && j(t),
                        t._h = 1),
                        !0 === s ? n = r : (l && l.enter(),
                        n = s(r),
                        l && (l.exit(),
                        a = !0)),
                        n === e.promise ? c(k("Promise-chain cycle")) : (i = O(n)) ? i.call(n, u, c) : u(n)) : c(r)
                    } catch (t) {
                        l && !a && l.exit(),
                        c(t)
                    }
                }; n.length > i; )
                    a(n[i++]);
                t._c = [],
                t._n = !1,
                e && !t._h && A(t)
            })
        }
    }, A = function(t) {
        y.call(u, function() {
            var e, n, r, o = t._v, i = D(t);
            if (i && (e = w(function() {
                T ? L.emit("unhandledRejection", o, t) : (n = u.onunhandledrejection) ? n({
                    promise: t,
                    reason: o
                }) : (r = u.console) && r.error && r.error("Unhandled promise rejection", o)
            }),
            t._h = T || D(t) ? 2 : 1),
            t._a = void 0,
            i && e.e)
                throw e.v
        })
    }, D = function(t) {
        return 1 !== t._h && 0 === (t._a || t._c).length
    }, j = function(t) {
        y.call(u, function() {
            var e;
            T ? L.emit("rejectionHandled", t) : (e = u.onrejectionhandled) && e({
                promise: t,
                reason: t._v
            })
        })
    }, G = function(t) {
        var e = this;
        e._d || (e._d = !0,
        (e = e._w || e)._v = t,
        e._s = 2,
        e._a || (e._a = e._c.slice()),
        P(e, !0))
    }, R = function(t) {
        var e, n = this;
        if (!n._d) {
            n._d = !0,
            n = n._w || n;
            try {
                if (n === t)
                    throw k("Promise can't be resolved itself");
                (e = O(t)) ? m(function() {
                    var r = {
                        _w: n,
                        _d: !1
                    };
                    try {
                        e.call(t, c(R, r, 1), c(G, r, 1))
                    } catch (t) {
                        G.call(r, t)
                    }
                }) : (n._v = t,
                n._s = 1,
                P(n, !1))
            } catch (t) {
                G.call({
                    _w: n,
                    _d: !1
                }, t)
            }
        }
    };
    I || (N = function(t) {
        p(this, N, "Promise", "_h"),
        d(t),
        r.call(this);
        try {
            t(c(R, this, 1), c(G, this, 1))
        } catch (t) {
            G.call(this, t)
        }
    }
    ,
    (r = function(t) {
        this._c = [],
        this._a = void 0,
        this._s = 0,
        this._d = !1,
        this._v = void 0,
        this._h = 0,
        this._n = !1
    }
    ).prototype = n(122)(N.prototype, {
        then: function(t, e) {
            var n = M(g(this, N));
            return n.ok = "function" != typeof t || t,
            n.fail = "function" == typeof e && e,
            n.domain = T ? L.domain : void 0,
            this._c.push(n),
            this._a && this._a.push(n),
            this._s && P(this, !1),
            n.promise
        },
        catch: function(t) {
            return this.then(void 0, t)
        }
    }),
    i = function() {
        var t = new r;
        this.promise = t,
        this.resolve = c(R, t, 1),
        this.reject = c(G, t, 1)
    }
    ,
    _.f = M = function(t) {
        return t === N || t === a ? new i(t) : o(t)
    }
    ),
    f(f.G + f.W + f.F * !I, {
        Promise: N
    }),
    n(29)(N, "Promise"),
    n(123)("Promise"),
    a = n(0).Promise,
    f(f.S + f.F * !I, "Promise", {
        reject: function(t) {
            var e = M(this);
            return (0,
            e.reject)(t),
            e.promise
        }
    }),
    f(f.S + f.F * (s || !I), "Promise", {
        resolve: function(t) {
            return b(s && this === a ? N : this, t)
        }
    }),
    f(f.S + f.F * !(I && n(80)(function(t) {
        N.all(t).catch(C)
    })), "Promise", {
        all: function(t) {
            var e = this
              , n = M(e)
              , r = n.resolve
              , o = n.reject
              , i = w(function() {
                var n = []
                  , i = 0
                  , a = 1;
                v(t, !1, function(t) {
                    var s = i++
                      , u = !1;
                    n.push(void 0),
                    a++,
                    e.resolve(t).then(function(t) {
                        u || (u = !0,
                        n[s] = t,
                        --a || r(n))
                    }, o)
                }),
                --a || r(n)
            });
            return i.e && o(i.v),
            n.promise
        },
        race: function(t) {
            var e = this
              , n = M(e)
              , r = n.reject
              , o = w(function() {
                v(t, !1, function(t) {
                    e.resolve(t).then(n.resolve, r)
                })
            });
            return o.e && r(o.v),
            n.promise
        }
    })
}
, function(t, e) {
    t.exports = function(t, e, n, r) {
        if (!(t instanceof e) || void 0 !== r && r in t)
            throw TypeError(n + ": incorrect invocation!");
        return t
    }
}
, function(t, e, n) {
    var r = n(20)
      , o = n(78)
      , i = n(79)
      , a = n(7)
      , s = n(53)
      , u = n(73)
      , c = {}
      , l = {};
    (e = t.exports = function(t, e, n, f, h) {
        var d, p, v, g, y = h ? function() {
            return t
        }
        : u(t), m = r(n, f, e ? 2 : 1), _ = 0;
        if ("function" != typeof y)
            throw TypeError(t + " is not iterable!");
        if (i(y)) {
            for (d = s(t.length); d > _; _++)
                if ((g = e ? m(a(p = t[_])[0], p[1]) : m(t[_])) === c || g === l)
                    return g
        } else
            for (v = y.call(t); !(p = v.next()).done; )
                if ((g = o(v, m, p.value, e)) === c || g === l)
                    return g
    }
    ).BREAK = c,
    e.RETURN = l
}
, function(t, e) {
    t.exports = function(t, e, n) {
        var r = void 0 === n;
        switch (e.length) {
        case 0:
            return r ? t() : t.call(n);
        case 1:
            return r ? t(e[0]) : t.call(n, e[0]);
        case 2:
            return r ? t(e[0], e[1]) : t.call(n, e[0], e[1]);
        case 3:
            return r ? t(e[0], e[1], e[2]) : t.call(n, e[0], e[1], e[2]);
        case 4:
            return r ? t(e[0], e[1], e[2], e[3]) : t.call(n, e[0], e[1], e[2], e[3])
        }
        return t.apply(n, e)
    }
}
, function(t, e, n) {
    var r = n(1)
      , o = n(69).set
      , i = r.MutationObserver || r.WebKitMutationObserver
      , a = r.process
      , s = r.Promise
      , u = "process" == n(24)(a);
    t.exports = function() {
        var t, e, n, c = function() {
            var r, o;
            for (u && (r = a.domain) && r.exit(); t; ) {
                o = t.fn,
                t = t.next;
                try {
                    o()
                } catch (r) {
                    throw t ? n() : e = void 0,
                    r
                }
            }
            e = void 0,
            r && r.enter()
        };
        if (u)
            n = function() {
                a.nextTick(c)
            }
            ;
        else if (!i || r.navigator && r.navigator.standalone)
            if (s && s.resolve) {
                var l = s.resolve(void 0);
                n = function() {
                    l.then(c)
                }
            } else
                n = function() {
                    o.call(r, c)
                }
                ;
        else {
            var f = !0
              , h = document.createTextNode("");
            new i(c).observe(h, {
                characterData: !0
            }),
            n = function() {
                h.data = f = !f
            }
        }
        return function(r) {
            var o = {
                fn: r,
                next: void 0
            };
            e && (e.next = o),
            t || (t = o,
            n()),
            e = o
        }
    }
}
, function(t, e, n) {
    var r = n(1).navigator;
    t.exports = r && r.userAgent || ""
}
, function(t, e, n) {
    var r = n(15);
    t.exports = function(t, e, n) {
        for (var o in e)
            n && t[o] ? t[o] = e[o] : r(t, o, e[o]);
        return t
    }
}
, function(t, e, n) {
    "use strict";
    var r = n(1)
      , o = n(0)
      , i = n(8)
      , a = n(9)
      , s = n(3)("species");
    t.exports = function(t) {
        var e = "function" == typeof o[t] ? o[t] : r[t];
        a && e && !e[s] && i.f(e, s, {
            configurable: !0,
            get: function() {
                return this
            }
        })
    }
}
, function(t, e, n) {
    "use strict";
    var r = n(6)
      , o = n(0)
      , i = n(1)
      , a = n(68)
      , s = n(71);
    r(r.P + r.R, "Promise", {
        finally: function(t) {
            var e = a(this, o.Promise || i.Promise)
              , n = "function" == typeof t;
            return this.then(n ? function(n) {
                return s(e, t()).then(function() {
                    return n
                })
            }
            : t, n ? function(n) {
                return s(e, t()).then(function() {
                    throw n
                })
            }
            : t)
        }
    })
}
, function(t, e, n) {
    "use strict";
    var r = n(6)
      , o = n(49)
      , i = n(70);
    r(r.S, "Promise", {
        try: function(t) {
            var e = o.f(this)
              , n = i(t);
            return (n.e ? e.reject : e.resolve)(n.v),
            e.promise
        }
    })
}
, function(t, e, n) {
    "use strict";
    t.exports = function() {
        var t = window
          , e = t.document;
        /constructor/i.test(t.HTMLElement) || t.safari,
        /CriOS\/[\d]+/.test(navigator.userAgent);
        return window.frameDownloadImg = function() {
            "about:blank" !== document.querySelector("#download_img_frame").src && window.frames.download_img_frame.document.execCommand("SaveAs")
        }
        ,
        function(n, r, o) {
            if (window.ActiveXObject || "ActiveXObject"in window)
                !function(t) {
                    var e = document.querySelector("#download_img_frame");
                    e || ((e = document.createElement("iframe")).style.display = "none",
                    e.id = "download_img_frame",
                    e.onload = "frameDownloadImg();",
                    e.src = "about:blank",
                    e.width = 0,
                    e.height = 0,
                    document.body.appendChild(e)),
                    (e = document.querySelector("#download_img_frame")).src !== t ? e.src = t : frameDownloadImg()
                }(n);
            else {
                var i = e.createElementNS("http://www.w3.org/1999/xhtml", "a");
                if ("download"in i && !o)
                    return i.href = n,
                    i.download = r,
                    document.body.appendChild(i),
                    void function(t) {
                        var e = new MouseEvent("click");
                        t.dispatchEvent(e),
                        setTimeout(function() {
                            document.removeChild(t)
                        }, 200)
                    }(i);
                t.open(n, "_blank") || (window.location.href = n)
            }
        }
    }
}
, function(t, e) {
    t.exports = function(t) {
        var e = "undefined" != typeof window && window.location;
        if (!e)
            throw new Error("fixUrls requires window.location");
        if (!t || "string" != typeof t)
            return t;
        var n = e.protocol + "//" + e.host
          , r = n + e.pathname.replace(/\/[^\/]*$/, "/");
        return t.replace(/url\s*\(((?:[^)(]|\((?:[^)(]+|\([^)(]*\))*\))*)\)/gi, function(t, e) {
            var o, i = e.trim().replace(/^"(.*)"$/, function(t, e) {
                return e
            }).replace(/^'(.*)'$/, function(t, e) {
                return e
            });
            return /^(#|data:|http:\/\/|https:\/\/|file:\/\/\/|\s*$)/i.test(i) ? t : (o = 0 === i.indexOf("//") ? i : 0 === i.indexOf("/") ? n + i : r + i.replace(/^\.\//, ""),
            "url(" + JSON.stringify(o) + ")")
        })
    }
}
, function(t, e, n) {
    t.exports = n(129)
}
, function(t, e, n) {
    var r = function() {
        return this
    }() || Function("return this")()
      , o = r.regeneratorRuntime && Object.getOwnPropertyNames(r).indexOf("regeneratorRuntime") >= 0
      , i = o && r.regeneratorRuntime;
    if (r.regeneratorRuntime = void 0,
    t.exports = n(130),
    o)
        r.regeneratorRuntime = i;
    else
        try {
            delete r.regeneratorRuntime
        } catch (t) {
            r.regeneratorRuntime = void 0
        }
}
, function(t, e) {
    !function(e) {
        "use strict";
        var n, r = Object.prototype, o = r.hasOwnProperty, i = "function" == typeof Symbol ? Symbol : {}, a = i.iterator || "@@iterator", s = i.asyncIterator || "@@asyncIterator", u = i.toStringTag || "@@toStringTag", c = "object" == typeof t, l = e.regeneratorRuntime;
        if (l)
            c && (t.exports = l);
        else {
            (l = e.regeneratorRuntime = c ? t.exports : {}).wrap = w;
            var f = "suspendedStart"
              , h = "suspendedYield"
              , d = "executing"
              , p = "completed"
              , v = {}
              , g = {};
            g[a] = function() {
                return this
            }
            ;
            var y = Object.getPrototypeOf
              , m = y && y(y(I([])));
            m && m !== r && o.call(m, a) && (g = m);
            var _ = L.prototype = b.prototype = Object.create(g);
            k.prototype = _.constructor = L,
            L.constructor = k,
            L[u] = k.displayName = "GeneratorFunction",
            l.isGeneratorFunction = function(t) {
                var e = "function" == typeof t && t.constructor;
                return !!e && (e === k || "GeneratorFunction" === (e.displayName || e.name))
            }
            ,
            l.mark = function(t) {
                return Object.setPrototypeOf ? Object.setPrototypeOf(t, L) : (t.__proto__ = L,
                u in t || (t[u] = "GeneratorFunction")),
                t.prototype = Object.create(_),
                t
            }
            ,
            l.awrap = function(t) {
                return {
                    __await: t
                }
            }
            ,
            E(S.prototype),
            S.prototype[s] = function() {
                return this
            }
            ,
            l.AsyncIterator = S,
            l.async = function(t, e, n, r) {
                var o = new S(w(t, e, n, r));
                return l.isGeneratorFunction(e) ? o : o.next().then(function(t) {
                    return t.done ? t.value : o.next()
                })
            }
            ,
            E(_),
            _[u] = "Generator",
            _[a] = function() {
                return this
            }
            ,
            _.toString = function() {
                return "[object Generator]"
            }
            ,
            l.keys = function(t) {
                var e = [];
                for (var n in t)
                    e.push(n);
                return e.reverse(),
                function n() {
                    for (; e.length; ) {
                        var r = e.pop();
                        if (r in t)
                            return n.value = r,
                            n.done = !1,
                            n
                    }
                    return n.done = !0,
                    n
                }
            }
            ,
            l.values = I,
            M.prototype = {
                constructor: M,
                reset: function(t) {
                    if (this.prev = 0,
                    this.next = 0,
                    this.sent = this._sent = n,
                    this.done = !1,
                    this.delegate = null,
                    this.method = "next",
                    this.arg = n,
                    this.tryEntries.forEach(C),
                    !t)
                        for (var e in this)
                            "t" === e.charAt(0) && o.call(this, e) && !isNaN(+e.slice(1)) && (this[e] = n)
                },
                stop: function() {
                    this.done = !0;
                    var t = this.tryEntries[0].completion;
                    if ("throw" === t.type)
                        throw t.arg;
                    return this.rval
                },
                dispatchException: function(t) {
                    if (this.done)
                        throw t;
                    var e = this;
                    function r(r, o) {
                        return s.type = "throw",
                        s.arg = t,
                        e.next = r,
                        o && (e.method = "next",
                        e.arg = n),
                        !!o
                    }
                    for (var i = this.tryEntries.length - 1; i >= 0; --i) {
                        var a = this.tryEntries[i]
                          , s = a.completion;
                        if ("root" === a.tryLoc)
                            return r("end");
                        if (a.tryLoc <= this.prev) {
                            var u = o.call(a, "catchLoc")
                              , c = o.call(a, "finallyLoc");
                            if (u && c) {
                                if (this.prev < a.catchLoc)
                                    return r(a.catchLoc, !0);
                                if (this.prev < a.finallyLoc)
                                    return r(a.finallyLoc)
                            } else if (u) {
                                if (this.prev < a.catchLoc)
                                    return r(a.catchLoc, !0)
                            } else {
                                if (!c)
                                    throw new Error("try statement without catch or finally");
                                if (this.prev < a.finallyLoc)
                                    return r(a.finallyLoc)
                            }
                        }
                    }
                },
                abrupt: function(t, e) {
                    for (var n = this.tryEntries.length - 1; n >= 0; --n) {
                        var r = this.tryEntries[n];
                        if (r.tryLoc <= this.prev && o.call(r, "finallyLoc") && this.prev < r.finallyLoc) {
                            var i = r;
                            break
                        }
                    }
                    i && ("break" === t || "continue" === t) && i.tryLoc <= e && e <= i.finallyLoc && (i = null);
                    var a = i ? i.completion : {};
                    return a.type = t,
                    a.arg = e,
                    i ? (this.method = "next",
                    this.next = i.finallyLoc,
                    v) : this.complete(a)
                },
                complete: function(t, e) {
                    if ("throw" === t.type)
                        throw t.arg;
                    return "break" === t.type || "continue" === t.type ? this.next = t.arg : "return" === t.type ? (this.rval = this.arg = t.arg,
                    this.method = "return",
                    this.next = "end") : "normal" === t.type && e && (this.next = e),
                    v
                },
                finish: function(t) {
                    for (var e = this.tryEntries.length - 1; e >= 0; --e) {
                        var n = this.tryEntries[e];
                        if (n.finallyLoc === t)
                            return this.complete(n.completion, n.afterLoc),
                            C(n),
                            v
                    }
                },
                catch: function(t) {
                    for (var e = this.tryEntries.length - 1; e >= 0; --e) {
                        var n = this.tryEntries[e];
                        if (n.tryLoc === t) {
                            var r = n.completion;
                            if ("throw" === r.type) {
                                var o = r.arg;
                                C(n)
                            }
                            return o
                        }
                    }
                    throw new Error("illegal catch attempt")
                },
                delegateYield: function(t, e, r) {
                    return this.delegate = {
                        iterator: I(t),
                        resultName: e,
                        nextLoc: r
                    },
                    "next" === this.method && (this.arg = n),
                    v
                }
            }
        }
        function w(t, e, n, r) {
            var o = e && e.prototype instanceof b ? e : b
              , i = Object.create(o.prototype)
              , a = new M(r || []);
            return i._invoke = function(t, e, n) {
                var r = f;
                return function(o, i) {
                    if (r === d)
                        throw new Error("Generator is already running");
                    if (r === p) {
                        if ("throw" === o)
                            throw i;
                        return O()
                    }
                    for (n.method = o,
                    n.arg = i; ; ) {
                        var a = n.delegate;
                        if (a) {
                            var s = N(a, n);
                            if (s) {
                                if (s === v)
                                    continue;
                                return s
                            }
                        }
                        if ("next" === n.method)
                            n.sent = n._sent = n.arg;
                        else if ("throw" === n.method) {
                            if (r === f)
                                throw r = p,
                                n.arg;
                            n.dispatchException(n.arg)
                        } else
                            "return" === n.method && n.abrupt("return", n.arg);
                        r = d;
                        var u = x(t, e, n);
                        if ("normal" === u.type) {
                            if (r = n.done ? p : h,
                            u.arg === v)
                                continue;
                            return {
                                value: u.arg,
                                done: n.done
                            }
                        }
                        "throw" === u.type && (r = p,
                        n.method = "throw",
                        n.arg = u.arg)
                    }
                }
            }(t, n, a),
            i
        }
        function x(t, e, n) {
            try {
                return {
                    type: "normal",
                    arg: t.call(e, n)
                }
            } catch (t) {
                return {
                    type: "throw",
                    arg: t
                }
            }
        }
        function b() {}
        function k() {}
        function L() {}
        function E(t) {
            ["next", "throw", "return"].forEach(function(e) {
                t[e] = function(t) {
                    return this._invoke(e, t)
                }
            })
        }
        function S(t) {
            var e;
            this._invoke = function(n, r) {
                function i() {
                    return new Promise(function(e, i) {
                        !function e(n, r, i, a) {
                            var s = x(t[n], t, r);
                            if ("throw" !== s.type) {
                                var u = s.arg
                                  , c = u.value;
                                return c && "object" == typeof c && o.call(c, "__await") ? Promise.resolve(c.__await).then(function(t) {
                                    e("next", t, i, a)
                                }, function(t) {
                                    e("throw", t, i, a)
                                }) : Promise.resolve(c).then(function(t) {
                                    u.value = t,
                                    i(u)
                                }, a)
                            }
                            a(s.arg)
                        }(n, r, e, i)
                    }
                    )
                }
                return e = e ? e.then(i, i) : i()
            }
        }
        function N(t, e) {
            var r = t.iterator[e.method];
            if (r === n) {
                if (e.delegate = null,
                "throw" === e.method) {
                    if (t.iterator.return && (e.method = "return",
                    e.arg = n,
                    N(t, e),
                    "throw" === e.method))
                        return v;
                    e.method = "throw",
                    e.arg = new TypeError("The iterator does not provide a 'throw' method")
                }
                return v
            }
            var o = x(r, t.iterator, e.arg);
            if ("throw" === o.type)
                return e.method = "throw",
                e.arg = o.arg,
                e.delegate = null,
                v;
            var i = o.arg;
            return i ? i.done ? (e[t.resultName] = i.value,
            e.next = t.nextLoc,
            "return" !== e.method && (e.method = "next",
            e.arg = n),
            e.delegate = null,
            v) : i : (e.method = "throw",
            e.arg = new TypeError("iterator result is not an object"),
            e.delegate = null,
            v)
        }
        function T(t) {
            var e = {
                tryLoc: t[0]
            };
            1 in t && (e.catchLoc = t[1]),
            2 in t && (e.finallyLoc = t[2],
            e.afterLoc = t[3]),
            this.tryEntries.push(e)
        }
        function C(t) {
            var e = t.completion || {};
            e.type = "normal",
            delete e.arg,
            t.completion = e
        }
        function M(t) {
            this.tryEntries = [{
                tryLoc: "root"
            }],
            t.forEach(T, this),
            this.reset(!0)
        }
        function I(t) {
            if (t) {
                var e = t[a];
                if (e)
                    return e.call(t);
                if ("function" == typeof t.next)
                    return t;
                if (!isNaN(t.length)) {
                    var r = -1
                      , i = function e() {
                        for (; ++r < t.length; )
                            if (o.call(t, r))
                                return e.value = t[r],
                                e.done = !1,
                                e;
                        return e.value = n,
                        e.done = !0,
                        e
                    };
                    return i.next = i
                }
            }
            return {
                next: O
            }
        }
        function O() {
            return {
                value: n,
                done: !0
            }
        }
    }(function() {
        return this
    }() || Function("return this")())
}
, function(t, e, n) {
    "use strict";
    e.__esModule = !0;
    var r = function(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }(n(19));
    e.default = function(t) {
        return function() {
            var e = t.apply(this, arguments);
            return new r.default(function(t, n) {
                return function o(i, a) {
                    try {
                        var s = e[i](a)
                          , u = s.value
                    } catch (t) {
                        return void n(t)
                    }
                    if (!s.done)
                        return r.default.resolve(u).then(function(t) {
                            o("next", t)
                        }, function(t) {
                            o("throw", t)
                        });
                    t(u)
                }("next")
            }
            )
        }
    }
}
, , , , function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = a(n(2))
      , o = a(n(4))
      , i = a(n(138));
    function a(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    var s = function() {
        function t() {
            (0,
            r.default)(this, t),
            this._bb = []
        }
        return (0,
        o.default)(t, [{
            key: "_tt",
            // _tt_=[[],[],[],[]]
            value: function(t, e, n) {
                n ? this._bb.push(n) : this._bb[t].push(e)
            }
        }, {
            key: "_ff",
            value: function(t) {
                return this._bb[t]
            }
        }]),
        t
    }();
    // flag
    e.default = function(t) {
        if ((t = String(t)) && t.length) {
            ",,06btf2,,0zl5whqisecpmu98y,,1,,118oszunvmb9fd7hcpy203j-ilktq46raw5exg,,,0kjrxn-034d1ao7vg,2s6h0pg3nmyldxeakzuf4rb-7oci8v219q,2wtj5,3x70digacthupf6veq4b5kw9s-jly3onzm21r8,4zj3l1us45gch7ot2ka-exybn8i6qp0drvmwf9,,68q-udk7tz4xfvwp2e9om5g1jin63rlbhycas0,5jhpx3d658ktlzb4nrvymga01c9-27qewusfoi,,,7d49moi5kqncs6bjyxlav3tuh-rz207gp8f1we,87-gx65nuqzwtm0hoypifks9lr12v4e8cbadj3,91t8zofl52yq9pgrxesd4nbuamchj3vi0-w7k6"
            var e = i.default.split(",")
              , n = new s;
            e.forEach(function(t) {
                var e = t.split("");//0,6,b,t,f,2
                if (e.length > 0)
                    for (var r = 1; r < e.length; r++)
                        n._tt(e[0], e[r]);
                else
                    n._tt(void 0, void 0, [])
            });
            var r = t.charCodeAt(0) + "";
            return r = r.length > 1 ? r[1] : r,
            n._ff(r)
        }
    }
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r, o = n(190), i = n(169), a = n(170), s = n(137), u = n(144), c = n(193), l = n(194);
    function f(t) {
        return void 0 !== t.leaves || void 0 !== t.groups
    }
    !function(t) {
        t[t.start = 0] = "start",
        t[t.tick = 1] = "tick",
        t[t.end = 2] = "end"
    }(r = e.EventType || (e.EventType = {}));
    var h = function() {
        function t() {
            var e = this;
            this._canvasSize = [1, 1],
            this._linkDistance = 20,
            this._defaultNodeSize = 10,
            this._linkLengthCalculator = null,
            this._linkType = null,
            this._avoidOverlaps = !1,
            this._handleDisconnected = !0,
            this._running = !1,
            this._nodes = [],
            this._groups = [],
            this._rootGroup = null,
            this._links = [],
            this._constraints = [],
            this._distanceMatrix = null,
            this._descent = null,
            this._directedLinkConstraints = null,
            this._threshold = .01,
            this._visibilityGraph = null,
            this._groupCompactness = 1e-6,
            this.event = null,
            this.linkAccessor = {
                getSourceIndex: t.getSourceIndex,
                getTargetIndex: t.getTargetIndex,
                setLength: t.setLinkLength,
                getType: function(t) {
                    return "function" == typeof e._linkType ? e._linkType(t) : 0
                }
            }
        }
        return t.prototype.on = function(t, e) {
            return this.event || (this.event = {}),
            "string" == typeof t ? this.event[r[t]] = e : this.event[t] = e,
            this
        }
        ,
        t.prototype.trigger = function(t) {
            this.event && void 0 !== this.event[t.type] && this.event[t.type](t)
        }
        ,
        t.prototype.kick = function() {
            for (; !this.tick(); )
                ;
        }
        ,
        t.prototype.tick = function() {
            if (this._alpha < this._threshold)
                return this._running = !1,
                this.trigger({
                    type: r.end,
                    alpha: this._alpha = 0,
                    stress: this._lastStress
                }),
                !0;
            var t, e, n = this._nodes.length;
            this._links.length;
            for (this._descent.locks.clear(),
            e = 0; e < n; ++e)
                if ((t = this._nodes[e]).fixed) {
                    void 0 !== t.px && void 0 !== t.py || (t.px = t.x,
                    t.py = t.y);
                    var o = [t.px, t.py];
                    this._descent.locks.add(e, o)
                }
            var i = this._descent.rungeKutta();
            return 0 === i ? this._alpha = 0 : void 0 !== this._lastStress && (this._alpha = i),
            this._lastStress = i,
            this.updateNodePositions(),
            this.trigger({
                type: r.tick,
                alpha: this._alpha,
                stress: this._lastStress
            }),
            !1
        }
        ,
        t.prototype.updateNodePositions = function() {
            for (var t, e = this._descent.x[0], n = this._descent.x[1], r = this._nodes.length; r--; )
                (t = this._nodes[r]).x = e[r],
                t.y = n[r]
        }
        ,
        t.prototype.nodes = function(t) {
            if (!t) {
                if (0 === this._nodes.length && this._links.length > 0) {
                    var e = 0;
                    this._links.forEach(function(t) {
                        e = Math.max(e, t.source, t.target)
                    }),
                    this._nodes = new Array(++e);
                    for (var n = 0; n < e; ++n)
                        this._nodes[n] = {}
                }
                return this._nodes
            }
            return this._nodes = t,
            this
        }
        ,
        t.prototype.groups = function(t) {
            var e = this;
            return t ? (this._groups = t,
            this._rootGroup = {},
            this._groups.forEach(function(t) {
                void 0 === t.padding && (t.padding = 1),
                void 0 !== t.leaves && t.leaves.forEach(function(n, r) {
                    "number" == typeof n && ((t.leaves[r] = e._nodes[n]).parent = t)
                }),
                void 0 !== t.groups && t.groups.forEach(function(n, r) {
                    "number" == typeof n && ((t.groups[r] = e._groups[n]).parent = t)
                })
            }),
            this._rootGroup.leaves = this._nodes.filter(function(t) {
                return void 0 === t.parent
            }),
            this._rootGroup.groups = this._groups.filter(function(t) {
                return void 0 === t.parent
            }),
            this) : this._groups
        }
        ,
        t.prototype.powerGraphGroups = function(t) {
            var e = o.getGroups(this._nodes, this._links, this.linkAccessor, this._rootGroup);
            return this.groups(e.groups),
            t(e),
            this
        }
        ,
        t.prototype.avoidOverlaps = function(t) {
            return arguments.length ? (this._avoidOverlaps = t,
            this) : this._avoidOverlaps
        }
        ,
        t.prototype.handleDisconnected = function(t) {
            return arguments.length ? (this._handleDisconnected = t,
            this) : this._handleDisconnected
        }
        ,
        t.prototype.flowLayout = function(t, e) {
            return arguments.length || (t = "y"),
            this._directedLinkConstraints = {
                axis: t,
                getMinSeparation: "number" == typeof e ? function() {
                    return e
                }
                : e
            },
            this
        }
        ,
        t.prototype.links = function(t) {
            return arguments.length ? (this._links = t,
            this) : this._links
        }
        ,
        t.prototype.constraints = function(t) {
            return arguments.length ? (this._constraints = t,
            this) : this._constraints
        }
        ,
        t.prototype.distanceMatrix = function(t) {
            return arguments.length ? (this._distanceMatrix = t,
            this) : this._distanceMatrix
        }
        ,
        t.prototype.size = function(t) {
            return t ? (this._canvasSize = t,
            this) : this._canvasSize
        }
        ,
        t.prototype.defaultNodeSize = function(t) {
            return t ? (this._defaultNodeSize = t,
            this) : this._defaultNodeSize
        }
        ,
        t.prototype.groupCompactness = function(t) {
            return t ? (this._groupCompactness = t,
            this) : this._groupCompactness
        }
        ,
        t.prototype.linkDistance = function(t) {
            return t ? (this._linkDistance = "function" == typeof t ? t : +t,
            this._linkLengthCalculator = null,
            this) : this._linkDistance
        }
        ,
        t.prototype.linkType = function(t) {
            return this._linkType = t,
            this
        }
        ,
        t.prototype.convergenceThreshold = function(t) {
            return t ? (this._threshold = "function" == typeof t ? t : +t,
            this) : this._threshold
        }
        ,
        t.prototype.alpha = function(t) {
            return arguments.length ? (t = +t,
            this._alpha ? this._alpha = t > 0 ? t : 0 : t > 0 && (this._running || (this._running = !0,
            this.trigger({
                type: r.start,
                alpha: this._alpha = t
            }),
            this.kick())),
            this) : this._alpha
        }
        ,
        t.prototype.getLinkLength = function(t) {
            return "function" == typeof this._linkDistance ? +this._linkDistance(t) : this._linkDistance
        }
        ,
        t.setLinkLength = function(t, e) {
            t.length = e
        }
        ,
        t.prototype.getLinkType = function(t) {
            return "function" == typeof this._linkType ? this._linkType(t) : 0
        }
        ,
        t.prototype.symmetricDiffLinkLengths = function(t, e) {
            var n = this;
            return void 0 === e && (e = 1),
            this.linkDistance(function(e) {
                return t * e.length
            }),
            this._linkLengthCalculator = function() {
                return i.symmetricDiffLinkLengths(n._links, n.linkAccessor, e)
            }
            ,
            this
        }
        ,
        t.prototype.jaccardLinkLengths = function(t, e) {
            var n = this;
            return void 0 === e && (e = 1),
            this.linkDistance(function(e) {
                return t * e.length
            }),
            this._linkLengthCalculator = function() {
                return i.jaccardLinkLengths(n._links, n.linkAccessor, e)
            }
            ,
            this
        }
        ,
        t.prototype.start = function(e, n, r, o, c) {
            var l = this;
            void 0 === e && (e = 0),
            void 0 === n && (n = 0),
            void 0 === r && (r = 0),
            void 0 === o && (o = 0),
            void 0 === c && (c = !0);
            var f, h = this.nodes().length, d = h + 2 * this._groups.length, p = (this._links.length,
            this._canvasSize[0]), v = this._canvasSize[1], g = new Array(d), y = new Array(d), m = null, _ = this._avoidOverlaps;
            this._nodes.forEach(function(t, e) {
                t.index = e,
                void 0 === t.x && (t.x = p / 2,
                t.y = v / 2),
                g[e] = t.x,
                y[e] = t.y
            }),
            this._linkLengthCalculator && this._linkLengthCalculator(),
            this._distanceMatrix ? f = this._distanceMatrix : (f = new u.Calculator(d,this._links,t.getSourceIndex,t.getTargetIndex,function(t) {
                return l.getLinkLength(t)
            }
            ).DistanceMatrix(),
            m = a.Descent.createSquareMatrix(d, function() {
                return 2
            }),
            this._links.forEach(function(t) {
                "number" == typeof t.source && (t.source = l._nodes[t.source]),
                "number" == typeof t.target && (t.target = l._nodes[t.target])
            }),
            this._links.forEach(function(e) {
                var n = t.getSourceIndex(e)
                  , r = t.getTargetIndex(e);
                m[n][r] = m[r][n] = e.weight || 1
            }));
            var w = a.Descent.createSquareMatrix(d, function(t, e) {
                return f[t][e]
            });
            if (this._rootGroup && void 0 !== this._rootGroup.groups) {
                var x = h;
                this._groups.forEach(function(t) {
                    !function(t, e, n, r) {
                        m[t][e] = m[e][t] = n,
                        w[t][e] = w[e][t] = r
                    }(x, x + 1, l._groupCompactness, .1),
                    g[x] = 0,
                    y[x++] = 0,
                    g[x] = 0,
                    y[x++] = 0
                })
            } else
                this._rootGroup = {
                    leaves: this._nodes,
                    groups: []
                };
            var b = this._constraints || [];
            this._directedLinkConstraints && (this.linkAccessor.getMinSeparation = this._directedLinkConstraints.getMinSeparation,
            b = b.concat(i.generateDirectedEdgeConstraints(h, this._links, this._directedLinkConstraints.axis, this.linkAccessor))),
            this.avoidOverlaps(!1),
            this._descent = new a.Descent([g, y],w),
            this._descent.locks.clear();
            for (x = 0; x < h; ++x) {
                var k = this._nodes[x];
                if (k.fixed) {
                    k.px = k.x,
                    k.py = k.y;
                    var L = [k.x, k.y];
                    this._descent.locks.add(x, L)
                }
            }
            if (this._descent.threshold = this._threshold,
            this.initialLayout(e, g, y),
            b.length > 0 && (this._descent.project = new s.Projection(this._nodes,this._groups,this._rootGroup,b).projectFunctions()),
            this._descent.run(n),
            this.separateOverlappingComponents(p, v),
            this.avoidOverlaps(_),
            _ && (this._nodes.forEach(function(t, e) {
                t.x = g[e],
                t.y = y[e]
            }),
            this._descent.project = new s.Projection(this._nodes,this._groups,this._rootGroup,b,!0).projectFunctions(),
            this._nodes.forEach(function(t, e) {
                g[e] = t.x,
                y[e] = t.y
            })),
            this._descent.G = m,
            this._descent.run(r),
            o) {
                this._descent.snapStrength = 1e3,
                this._descent.snapGridSize = this._nodes[0].width,
                this._descent.numGridSnapNodes = h,
                this._descent.scaleSnapByMaxH = h != d;
                var E = a.Descent.createSquareMatrix(d, function(t, e) {
                    return t >= h || e >= h ? m[t][e] : 0
                });
                this._descent.G = E,
                this._descent.run(o)
            }
            return this.updateNodePositions(),
            this.separateOverlappingComponents(p, v),
            c ? this.resume() : this
        }
        ,
        t.prototype.initialLayout = function(e, n, r) {
            if (this._groups.length > 0 && e > 0) {
                var o = this._nodes.length
                  , i = this._links.map(function(t) {
                    return {
                        source: t.source.index,
                        target: t.target.index
                    }
                })
                  , a = this._nodes.map(function(t) {
                    return {
                        index: t.index
                    }
                });
                this._groups.forEach(function(t, e) {
                    a.push({
                        index: t.index = o + e
                    })
                }),
                this._groups.forEach(function(t, e) {
                    void 0 !== t.leaves && t.leaves.forEach(function(e) {
                        return i.push({
                            source: t.index,
                            target: e.index
                        })
                    }),
                    void 0 !== t.groups && t.groups.forEach(function(e) {
                        return i.push({
                            source: t.index,
                            target: e.index
                        })
                    })
                }),
                (new t).size(this.size()).nodes(a).links(i).avoidOverlaps(!1).linkDistance(this.linkDistance()).symmetricDiffLinkLengths(5).convergenceThreshold(1e-4).start(e, 0, 0, 0, !1),
                this._nodes.forEach(function(t) {
                    n[t.index] = a[t.index].x,
                    r[t.index] = a[t.index].y
                })
            } else
                this._descent.run(e)
        }
        ,
        t.prototype.separateOverlappingComponents = function(t, e) {
            var n = this;
            if (!this._distanceMatrix && this._handleDisconnected) {
                var r = this._descent.x[0]
                  , o = this._descent.x[1];
                this._nodes.forEach(function(t, e) {
                    t.x = r[e],
                    t.y = o[e]
                });
                var i = l.separateGraphs(this._nodes, this._links);
                l.applyPacking(i, t, e, this._defaultNodeSize),
                this._nodes.forEach(function(t, e) {
                    n._descent.x[0][e] = t.x,
                    n._descent.x[1][e] = t.y,
                    t.bounds && (t.bounds.setXCentre(t.x),
                    t.bounds.setYCentre(t.y))
                })
            }
        }
        ,
        t.prototype.resume = function() {
            return this.alpha(.1)
        }
        ,
        t.prototype.stop = function() {
            return this.alpha(0)
        }
        ,
        t.prototype.prepareEdgeRouting = function(t) {
            void 0 === t && (t = 0),
            this._visibilityGraph = new c.TangentVisibilityGraph(this._nodes.map(function(e) {
                return e.bounds.inflate(-t).vertices()
            }))
        }
        ,
        t.prototype.routeEdge = function(t, e, n) {
            void 0 === e && (e = 5);
            var r = []
              , o = new c.TangentVisibilityGraph(this._visibilityGraph.P,{
                V: this._visibilityGraph.V,
                E: this._visibilityGraph.E
            })
              , i = {
                x: t.source.x,
                y: t.source.y
            }
              , a = {
                x: t.target.x,
                y: t.target.y
            }
              , l = o.addPoint(i, t.source.index)
              , f = o.addPoint(a, t.target.index);
            o.addEdgeIfVisible(i, a, t.source.index, t.target.index),
            void 0 !== n && n(o);
            var h = new u.Calculator(o.V.length,o.E,function(t) {
                return t.source.id
            }
            ,function(t) {
                return t.target.id
            }
            ,function(t) {
                return t.length()
            }
            ).PathFromNodeToNode(l.id, f.id);
            if (1 === h.length || h.length === o.V.length) {
                var d = s.makeEdgeBetween(t.source.innerBounds, t.target.innerBounds, e);
                r = [d.sourceIntersection, d.arrowStart]
            } else {
                for (var p = h.length - 2, v = o.V[h[p]].p, g = o.V[h[0]].p, y = (r = [t.source.innerBounds.rayIntersection(v.x, v.y)],
                p); y >= 0; --y)
                    r.push(o.V[h[y]].p);
                r.push(s.makeEdgeTo(g, t.target.innerBounds, e))
            }
            return r
        }
        ,
        t.getSourceIndex = function(t) {
            return "number" == typeof t.source ? t.source : t.source.index
        }
        ,
        t.getTargetIndex = function(t) {
            return "number" == typeof t.target ? t.target : t.target.index
        }
        ,
        t.linkId = function(e) {
            return t.getSourceIndex(e) + "-" + t.getTargetIndex(e)
        }
        ,
        t.dragStart = function(e) {
            f(e) ? t.storeOffset(e, t.dragOrigin(e)) : (t.stopNode(e),
            e.fixed |= 2)
        }
        ,
        t.stopNode = function(t) {
            t.px = t.x,
            t.py = t.y
        }
        ,
        t.storeOffset = function(e, n) {
            void 0 !== e.leaves && e.leaves.forEach(function(e) {
                e.fixed |= 2,
                t.stopNode(e),
                e._dragGroupOffsetX = e.x - n.x,
                e._dragGroupOffsetY = e.y - n.y
            }),
            void 0 !== e.groups && e.groups.forEach(function(e) {
                return t.storeOffset(e, n)
            })
        }
        ,
        t.dragOrigin = function(t) {
            return f(t) ? {
                x: t.bounds.cx(),
                y: t.bounds.cy()
            } : t
        }
        ,
        t.drag = function(e, n) {
            f(e) ? (void 0 !== e.leaves && e.leaves.forEach(function(t) {
                e.bounds.setXCentre(n.x),
                e.bounds.setYCentre(n.y),
                t.px = t._dragGroupOffsetX + n.x,
                t.py = t._dragGroupOffsetY + n.y
            }),
            void 0 !== e.groups && e.groups.forEach(function(e) {
                return t.drag(e, n)
            })) : (e.px = n.x,
            e.py = n.y)
        }
        ,
        t.dragEnd = function(e) {
            f(e) ? (void 0 !== e.leaves && e.leaves.forEach(function(e) {
                t.dragEnd(e),
                delete e._dragGroupOffsetX,
                delete e._dragGroupOffsetY
            }),
            void 0 !== e.groups && e.groups.forEach(t.dragEnd)) : e.fixed &= -7
        }
        ,
        t.mouseOver = function(t) {
            t.fixed |= 4,
            t.px = t.x,
            t.py = t.y
        }
        ,
        t.mouseOut = function(t) {
            t.fixed &= -5
        }
        ,
        t
    }();
    e.Layout = h
}
, function(t, e, n) {
    "use strict";
    var r = this && this.__extends || function() {
        var t = Object.setPrototypeOf || {
            __proto__: []
        }instanceof Array && function(t, e) {
            t.__proto__ = e
        }
        || function(t, e) {
            for (var n in e)
                e.hasOwnProperty(n) && (t[n] = e[n])
        }
        ;
        return function(e, n) {
            function r() {
                this.constructor = e
            }
            t(e, n),
            e.prototype = null === n ? Object.create(n) : (r.prototype = n.prototype,
            new r)
        }
    }();
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var o = n(171)
      , i = n(191);
    function a(t) {
        return t.bounds = void 0 !== t.leaves ? t.leaves.reduce(function(t, e) {
            return e.bounds.union(t)
        }, s.empty()) : s.empty(),
        void 0 !== t.groups && (t.bounds = t.groups.reduce(function(t, e) {
            return a(e).union(t)
        }, t.bounds)),
        t.bounds = t.bounds.inflate(t.padding),
        t.bounds
    }
    e.computeGroupBounds = a;
    var s = function() {
        function t(t, e, n, r) {
            this.x = t,
            this.X = e,
            this.y = n,
            this.Y = r
        }
        return t.empty = function() {
            return new t(Number.POSITIVE_INFINITY,Number.NEGATIVE_INFINITY,Number.POSITIVE_INFINITY,Number.NEGATIVE_INFINITY)
        }
        ,
        t.prototype.cx = function() {
            return (this.x + this.X) / 2
        }
        ,
        t.prototype.cy = function() {
            return (this.y + this.Y) / 2
        }
        ,
        t.prototype.overlapX = function(t) {
            var e = this.cx()
              , n = t.cx();
            return e <= n && t.x < this.X ? this.X - t.x : n <= e && this.x < t.X ? t.X - this.x : 0
        }
        ,
        t.prototype.overlapY = function(t) {
            var e = this.cy()
              , n = t.cy();
            return e <= n && t.y < this.Y ? this.Y - t.y : n <= e && this.y < t.Y ? t.Y - this.y : 0
        }
        ,
        t.prototype.setXCentre = function(t) {
            var e = t - this.cx();
            this.x += e,
            this.X += e
        }
        ,
        t.prototype.setYCentre = function(t) {
            var e = t - this.cy();
            this.y += e,
            this.Y += e
        }
        ,
        t.prototype.width = function() {
            return this.X - this.x
        }
        ,
        t.prototype.height = function() {
            return this.Y - this.y
        }
        ,
        t.prototype.union = function(e) {
            return new t(Math.min(this.x, e.x),Math.max(this.X, e.X),Math.min(this.y, e.y),Math.max(this.Y, e.Y))
        }
        ,
        t.prototype.lineIntersections = function(e, n, r, o) {
            for (var i = [[this.x, this.y, this.X, this.y], [this.X, this.y, this.X, this.Y], [this.X, this.Y, this.x, this.Y], [this.x, this.Y, this.x, this.y]], a = [], s = 0; s < 4; ++s) {
                var u = t.lineIntersection(e, n, r, o, i[s][0], i[s][1], i[s][2], i[s][3]);
                null !== u && a.push({
                    x: u.x,
                    y: u.y
                })
            }
            return a
        }
        ,
        t.prototype.rayIntersection = function(t, e) {
            var n = this.lineIntersections(this.cx(), this.cy(), t, e);
            return n.length > 0 ? n[0] : null
        }
        ,
        t.prototype.vertices = function() {
            return [{
                x: this.x,
                y: this.y
            }, {
                x: this.X,
                y: this.y
            }, {
                x: this.X,
                y: this.Y
            }, {
                x: this.x,
                y: this.Y
            }]
        }
        ,
        t.lineIntersection = function(t, e, n, r, o, i, a, s) {
            var u = n - t
              , c = a - o
              , l = r - e
              , f = s - i
              , h = f * u - c * l;
            if (0 == h)
                return null;
            var d = t - o
              , p = e - i
              , v = (c * p - f * d) / h
              , g = (u * p - l * d) / h;
            return v >= 0 && v <= 1 && g >= 0 && g <= 1 ? {
                x: t + v * u,
                y: e + v * l
            } : null
        }
        ,
        t.prototype.inflate = function(e) {
            return new t(this.x - e,this.X + e,this.y - e,this.Y + e)
        }
        ,
        t
    }();
    e.Rectangle = s,
    e.makeEdgeBetween = function(t, e, n) {
        var r = t.rayIntersection(e.cx(), e.cy()) || {
            x: t.cx(),
            y: t.cy()
        }
          , o = e.rayIntersection(t.cx(), t.cy()) || {
            x: e.cx(),
            y: e.cy()
        }
          , i = o.x - r.x
          , a = o.y - r.y
          , s = Math.sqrt(i * i + a * a)
          , u = s - n;
        return {
            sourceIntersection: r,
            targetIntersection: o,
            arrowStart: {
                x: r.x + u * i / s,
                y: r.y + u * a / s
            }
        }
    }
    ,
    e.makeEdgeTo = function(t, e, n) {
        var r = e.rayIntersection(t.x, t.y);
        r || (r = {
            x: e.cx(),
            y: e.cy()
        });
        var o = r.x - t.x
          , i = r.y - t.y
          , a = Math.sqrt(o * o + i * i);
        return {
            x: r.x - n * o / a,
            y: r.y - n * i / a
        }
    }
    ;
    var u = function() {
        return function(t, e, n) {
            this.v = t,
            this.r = e,
            this.pos = n,
            this.prev = f(),
            this.next = f()
        }
    }()
      , c = function() {
        return function(t, e, n) {
            this.isOpen = t,
            this.v = e,
            this.pos = n
        }
    }();
    function l(t, e) {
        return t.pos > e.pos ? 1 : t.pos < e.pos ? -1 : t.isOpen ? -1 : e.isOpen ? 1 : 0
    }
    function f() {
        return new i.RBTree(function(t, e) {
            return t.pos - e.pos
        }
        )
    }
    var h = {
        getCentre: function(t) {
            return t.cx()
        },
        getOpen: function(t) {
            return t.y
        },
        getClose: function(t) {
            return t.Y
        },
        getSize: function(t) {
            return t.width()
        },
        makeRect: function(t, e, n, r) {
            return new s(n - r / 2,n + r / 2,t,e)
        },
        findNeighbours: function(t, e) {
            var n = function(n, r) {
                for (var o, i = e.findIter(t); null !== (o = i[n]()); ) {
                    var a = o.r.overlapX(t.r);
                    if ((a <= 0 || a <= o.r.overlapY(t.r)) && (t[n].insert(o),
                    o[r].insert(t)),
                    a <= 0)
                        break
                }
            };
            n("next", "prev"),
            n("prev", "next")
        }
    }
      , d = {
        getCentre: function(t) {
            return t.cy()
        },
        getOpen: function(t) {
            return t.x
        },
        getClose: function(t) {
            return t.X
        },
        getSize: function(t) {
            return t.height()
        },
        makeRect: function(t, e, n, r) {
            return new s(t,e,n - r / 2,n + r / 2)
        },
        findNeighbours: function(t, e) {
            var n = function(n, r) {
                var o = e.findIter(t)[n]();
                null !== o && o.r.overlapX(t.r) > 0 && (t[n].insert(o),
                o[r].insert(t))
            };
            n("next", "prev"),
            n("prev", "next")
        }
    };
    function p(t, e, n, r) {
        void 0 === r && (r = !1);
        var o = t.padding
          , i = void 0 !== t.groups ? t.groups.length : 0
          , a = void 0 !== t.leaves ? t.leaves.length : 0
          , s = i ? t.groups.reduce(function(t, r) {
            return t.concat(p(r, e, n, !0))
        }, []) : []
          , u = (r ? 2 : 0) + a + i
          , c = new Array(u)
          , l = new Array(u)
          , f = 0
          , h = function(t, e) {
            l[f] = t,
            c[f++] = e
        };
        if (r) {
            var d = t.bounds
              , g = e.getCentre(d)
              , y = e.getSize(d) / 2
              , m = e.getOpen(d)
              , _ = e.getClose(d)
              , w = g - y + o / 2
              , x = g + y - o / 2;
            t.minVar.desiredPosition = w,
            h(e.makeRect(m, _, w, o), t.minVar),
            t.maxVar.desiredPosition = x,
            h(e.makeRect(m, _, x, o), t.maxVar)
        }
        a && t.leaves.forEach(function(t) {
            return h(t.bounds, t.variable)
        }),
        i && t.groups.forEach(function(t) {
            var n = t.bounds;
            h(e.makeRect(e.getOpen(n), e.getClose(n), e.getCentre(n), e.getSize(n)), t.minVar)
        });
        var b = v(l, c, e, n);
        return i && (c.forEach(function(t) {
            t.cOut = [],
            t.cIn = []
        }),
        b.forEach(function(t) {
            t.left.cOut.push(t),
            t.right.cIn.push(t)
        }),
        t.groups.forEach(function(t) {
            var n = (t.padding - e.getSize(t.bounds)) / 2;
            t.minVar.cIn.forEach(function(t) {
                return t.gap += n
            }),
            t.minVar.cOut.forEach(function(e) {
                e.left = t.maxVar,
                e.gap += n
            })
        })),
        s.concat(b)
    }
    function v(t, e, n, r) {
        var i, a = t.length, s = 2 * a;
        console.assert(e.length >= a);
        var h = new Array(s);
        for (i = 0; i < a; ++i) {
            var d = t[i]
              , p = new u(e[i],d,n.getCentre(d));
            h[i] = new c(!0,p,n.getOpen(d)),
            h[i + a] = new c(!1,p,n.getClose(d))
        }
        h.sort(l);
        var v = new Array
          , g = f();
        for (i = 0; i < s; ++i) {
            var y = h[i];
            p = y.v;
            if (y.isOpen)
                g.insert(p),
                n.findNeighbours(p, g);
            else {
                g.remove(p);
                var m = function(t, e) {
                    var i = (n.getSize(t.r) + n.getSize(e.r)) / 2 + r;
                    v.push(new o.Constraint(t.v,e.v,i))
                }
                  , _ = function(t, e, n) {
                    for (var r, o = p[t].iterator(); null !== (r = o[t]()); )
                        n(r, p),
                        r[e].remove(p)
                };
                _("prev", "next", function(t, e) {
                    return m(t, e)
                }),
                _("next", "prev", function(t, e) {
                    return m(e, t)
                })
            }
        }
        return console.assert(0 === g.size),
        v
    }
    function g(t, e) {
        return v(t, e, h, 1e-6)
    }
    function y(t, e) {
        return v(t, e, d, 1e-6)
    }
    function m(t) {
        return p(t, h, 1e-6)
    }
    function _(t) {
        return p(t, d, 1e-6)
    }
    e.generateXConstraints = g,
    e.generateYConstraints = y,
    e.generateXGroupConstraints = m,
    e.generateYGroupConstraints = _,
    e.removeOverlaps = function(t) {
        var e = t.map(function(t) {
            return new o.Variable(t.cx())
        })
          , n = g(t, e)
          , r = new o.Solver(e,n);
        r.solve(),
        e.forEach(function(e, n) {
            return t[n].setXCentre(e.position())
        }),
        e = t.map(function(t) {
            return new o.Variable(t.cy())
        }),
        n = y(t, e),
        (r = new o.Solver(e,n)).solve(),
        e.forEach(function(e, n) {
            return t[n].setYCentre(e.position())
        })
    }
    ;
    var w = function(t) {
        function e(e, n) {
            var r = t.call(this, 0, n) || this;
            return r.index = e,
            r
        }
        return r(e, t),
        e
    }(o.Variable);
    e.IndexedVariable = w;
    var x = function() {
        function t(t, e, n, r, o) {
            void 0 === n && (n = null),
            void 0 === r && (r = null),
            void 0 === o && (o = !1);
            var i = this;
            if (this.nodes = t,
            this.groups = e,
            this.rootGroup = n,
            this.avoidOverlaps = o,
            this.variables = t.map(function(t, e) {
                return t.variable = new w(e,1)
            }),
            r && this.createConstraints(r),
            o && n && void 0 !== n.groups) {
                t.forEach(function(t) {
                    if (t.width && t.height) {
                        var e = t.width / 2
                          , n = t.height / 2;
                        t.bounds = new s(t.x - e,t.x + e,t.y - n,t.y + n)
                    } else
                        t.bounds = new s(t.x,t.x,t.y,t.y)
                }),
                a(n);
                var u = t.length;
                e.forEach(function(t) {
                    i.variables[u] = t.minVar = new w(u++,void 0 !== t.stiffness ? t.stiffness : .01),
                    i.variables[u] = t.maxVar = new w(u++,void 0 !== t.stiffness ? t.stiffness : .01)
                })
            }
        }
        return t.prototype.createSeparation = function(t) {
            return new o.Constraint(this.nodes[t.left].variable,this.nodes[t.right].variable,t.gap,void 0 !== t.equality && t.equality)
        }
        ,
        t.prototype.makeFeasible = function(t) {
            var e = this;
            if (this.avoidOverlaps) {
                var n = "x"
                  , r = "width";
                "x" === t.axis && (n = "y",
                r = "height");
                var o = null;
                t.offsets.map(function(t) {
                    return e.nodes[t.node]
                }).sort(function(t, e) {
                    return t[n] - e[n]
                }).forEach(function(t) {
                    if (o) {
                        var e = o[n] + o[r];
                        e > t[n] && (t[n] = e)
                    }
                    o = t
                })
            }
        }
        ,
        t.prototype.createAlignment = function(t) {
            var e = this
              , n = this.nodes[t.offsets[0].node].variable;
            this.makeFeasible(t);
            var r = "x" === t.axis ? this.xConstraints : this.yConstraints;
            t.offsets.slice(1).forEach(function(t) {
                var i = e.nodes[t.node].variable;
                r.push(new o.Constraint(n,i,t.offset,!0))
            })
        }
        ,
        t.prototype.createConstraints = function(t) {
            var e = this
              , n = function(t) {
                return void 0 === t.type || "separation" === t.type
            };
            this.xConstraints = t.filter(function(t) {
                return "x" === t.axis && n(t)
            }).map(function(t) {
                return e.createSeparation(t)
            }),
            this.yConstraints = t.filter(function(t) {
                return "y" === t.axis && n(t)
            }).map(function(t) {
                return e.createSeparation(t)
            }),
            t.filter(function(t) {
                return "alignment" === t.type
            }).forEach(function(t) {
                return e.createAlignment(t)
            })
        }
        ,
        t.prototype.setupVariablesAndBounds = function(t, e, n, r) {
            this.nodes.forEach(function(o, i) {
                o.fixed ? (o.variable.weight = o.fixedWeight ? o.fixedWeight : 1e3,
                n[i] = r(o)) : o.variable.weight = 1;
                var a = (o.width || 0) / 2
                  , u = (o.height || 0) / 2
                  , c = t[i]
                  , l = e[i];
                o.bounds = new s(c - a,c + a,l - u,l + u)
            })
        }
        ,
        t.prototype.xProject = function(t, e, n) {
            (this.rootGroup || this.avoidOverlaps || this.xConstraints) && this.project(t, e, t, n, function(t) {
                return t.px
            }, this.xConstraints, m, function(t) {
                return t.bounds.setXCentre(n[t.variable.index] = t.variable.position())
            }, function(t) {
                var e = n[t.minVar.index] = t.minVar.position()
                  , r = n[t.maxVar.index] = t.maxVar.position()
                  , o = t.padding / 2;
                t.bounds.x = e - o,
                t.bounds.X = r + o
            })
        }
        ,
        t.prototype.yProject = function(t, e, n) {
            (this.rootGroup || this.yConstraints) && this.project(t, e, e, n, function(t) {
                return t.py
            }, this.yConstraints, _, function(t) {
                return t.bounds.setYCentre(n[t.variable.index] = t.variable.position())
            }, function(t) {
                var e = n[t.minVar.index] = t.minVar.position()
                  , r = n[t.maxVar.index] = t.maxVar.position()
                  , o = t.padding / 2;
                t.bounds.y = e - o,
                t.bounds.Y = r + o
            })
        }
        ,
        t.prototype.projectFunctions = function() {
            var t = this;
            return [function(e, n, r) {
                return t.xProject(e, n, r)
            }
            , function(e, n, r) {
                return t.yProject(e, n, r)
            }
            ]
        }
        ,
        t.prototype.project = function(t, e, n, r, o, i, s, u, c) {
            this.setupVariablesAndBounds(t, e, r, o),
            this.rootGroup && this.avoidOverlaps && (a(this.rootGroup),
            i = i.concat(s(this.rootGroup))),
            this.solve(this.variables, i, n, r),
            this.nodes.forEach(u),
            this.rootGroup && this.avoidOverlaps && (this.groups.forEach(c),
            a(this.rootGroup))
        }
        ,
        t.prototype.solve = function(t, e, n, r) {
            var i = new o.Solver(t,e);
            i.setStartingPositions(n),
            i.setDesiredPositions(r),
            i.solve()
        }
        ,
        t
    }();
    e.Projection = x
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    }),
    e.default = ",,06btf2,,0zl5whqisecpmu98y,,1,,118oszunvmb9fd7hcpy203j-ilktq46raw5exg,,,0kjrxn-034d1ao7vg,2s6h0pg3nmyldxeakzuf4rb-7oci8v219q,2wtj5,3x70digacthupf6veq4b5kw9s-jly3onzm21r8,4zj3l1us45gch7ot2ka-exybn8i6qp0drvmwf9,,68q-udk7tz4xfvwp2e9om5g1jin63rlbhycas0,5jhpx3d658ktlzb4nrvymga01c9-27qewusfoi,,,7d49moi5kqncs6bjyxlav3tuh-rz207gp8f1we,87-gx65nuqzwtm0hoypifks9lr12v4e8cbadj3,91t8zofl52yq9pgrxesd4nbuamchj3vi0-w7k6"
}
, , , , , function(t, e, n) {
    t.exports = {
        default: n(165),
        __esModule: !0
    }
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = n(192)
      , o = function() {
        return function(t, e) {
            this.id = t,
            this.distance = e
        }
    }()
      , i = function() {
        return function(t) {
            this.id = t,
            this.neighbours = []
        }
    }()
      , a = function() {
        return function(t, e, n) {
            this.node = t,
            this.prev = e,
            this.d = n
        }
    }()
      , s = function() {
        function t(t, e, n, r, a) {
            this.n = t,
            this.es = e,
            this.neighbours = new Array(this.n);
            for (var s = this.n; s--; )
                this.neighbours[s] = new i(s);
            for (s = this.es.length; s--; ) {
                var u = this.es[s]
                  , c = n(u)
                  , l = r(u)
                  , f = a(u);
                this.neighbours[c].neighbours.push(new o(l,f)),
                this.neighbours[l].neighbours.push(new o(c,f))
            }
        }
        return t.prototype.DistanceMatrix = function() {
            for (var t = new Array(this.n), e = 0; e < this.n; ++e)
                t[e] = this.dijkstraNeighbours(e);
            return t
        }
        ,
        t.prototype.DistancesFromNode = function(t) {
            return this.dijkstraNeighbours(t)
        }
        ,
        t.prototype.PathFromNodeToNode = function(t, e) {
            return this.dijkstraNeighbours(t, e)
        }
        ,
        t.prototype.PathFromNodeToNodeWithPrevCost = function(t, e, n) {
            var o = new r.PriorityQueue(function(t, e) {
                return t.d <= e.d
            }
            )
              , i = this.neighbours[t]
              , s = new a(i,null,0)
              , u = {};
            for (o.push(s); !o.empty() && (i = (s = o.pop()).node).id !== e; )
                for (var c = i.neighbours.length; c--; ) {
                    var l = i.neighbours[c]
                      , f = this.neighbours[l.id];
                    if (!s.prev || f.id !== s.prev.node.id) {
                        var h = f.id + "," + i.id;
                        if (!(h in u && u[h] <= s.d)) {
                            var d = s.prev ? n(s.prev.node.id, i.id, f.id) : 0
                              , p = s.d + l.distance + d;
                            u[h] = p,
                            o.push(new a(f,s,p))
                        }
                    }
                }
            for (var v = []; s.prev; )
                s = s.prev,
                v.push(s.node.id);
            return v
        }
        ,
        t.prototype.dijkstraNeighbours = function(t, e) {
            void 0 === e && (e = -1);
            for (var n = new r.PriorityQueue(function(t, e) {
                return t.d <= e.d
            }
            ), o = this.neighbours.length, i = new Array(o); o--; ) {
                var a = this.neighbours[o];
                a.d = o === t ? 0 : Number.POSITIVE_INFINITY,
                a.q = n.push(a)
            }
            for (; !n.empty(); ) {
                var s = n.pop();
                if (i[s.id] = s.d,
                s.id === e) {
                    for (var u = [], c = s; void 0 !== c.prev; )
                        u.push(c.prev.id),
                        c = c.prev;
                    return u
                }
                for (o = s.neighbours.length; o--; ) {
                    var l = s.neighbours[o]
                      , f = (c = this.neighbours[l.id],
                    s.d + l.distance);
                    s.d !== Number.MAX_VALUE && c.d > f && (c.d = f,
                    c.prev = s,
                    n.reduceKey(c.q, c, function(t, e) {
                        return t.q = e
                    }))
                }
            }
            return i
        }
        ,
        t
    }();
    e.Calculator = s
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    e.NodeTypeMap = {
        human: {
            color: "#F25A29",
            icon: "tpp-users",
            text: "个人"
        },
        company: {
            color: "#2394ce",
            icon: "tpp-building",
            text: "公司"
        },
        lawsuit: {
            color: "#2394ce",
            text: "法律诉讼"
        },
        announcement: {
            color: "#2394ce",
            text: "法院公告"
        },
        dishonest: {
            color: "#2394ce",
            text: "失信人"
        },
        courtnotices: {
            color: "#2394ce",
            text: "开庭公告"
        },
        judicialsale: {
            color: "#2394ce",
            text: "司法拍卖"
        },
        bid: {
            color: "#2394ce",
            text: "招投标"
        },
        tm: {
            color: "#2394ce",
            text: "商标信息"
        }
    },
    e.LinkTypeMap = {
        invest_c: {
            color: "#F25A29",
            text: "企业投资"
        },
        invest_h: {
            color: "#F25A29",
            text: "个人投资"
        },
        invest: {
            color: "#F25A29",
            text: "投资"
        },
        own: {
            color: "#cce198",
            text: "法人"
        },
        own_c: {
            color: "#cce198",
            text: "法人(企业)"
        },
        branch: {
            color: "#91abd1",
            text: "分支"
        },
        serve: {
            color: "#80c2d8",
            text: "任职"
        },
        serve_all: {
            color: "#80c2d8",
            text: "任职"
        },
        dishonest: {
            color: "#FF6C7C",
            text: "失信人"
        },
        lawsuit: {
            color: "#e66b7a",
            text: "诉讼"
        },
        law: {
            color: "#e66b7a",
            text: "诉讼"
        },
        tm_relation: {
            color: "#837af2",
            text: "商标"
        },
        announcement: {
            color: "#cc7ae7",
            text: "法院公告"
        },
        courtnotices: {
            color: "#ff3b30",
            text: "开庭公告"
        },
        companybid: {
            color: "#b3d465",
            text: "招投标"
        },
        judicialsale: {
            color: "#ffa030",
            text: "司法拍卖"
        },
        cac: {
            color: "#837af2",
            text: "竞合"
        },
        eq: {
            color: "#e012cb",
            text: "债务"
        },
        null: {
            color: "#D4D6D7",
            text: "未知"
        }
    }
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    e.ACTION_TOGGLE_LINK_TYPE = "RELATION_LEGENDS_ACTION_TOGGLE_LINK_TYPE",
    e.ACTION_MOUSE_IN_NODE = "RELATION_LEGENDS_ACTION_MOUSE_IN_NODE",
    e.ACTION_MOUSE_LEAVENODE = "RELATION_LEGENDS_ACTION_MOUSE_LEAVENODE"
}
, , , , , , , , , , function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    e.ACTION_CURRENT_DETAIL = "ACTION_CURRENT_DETAIL"
}
, , , function(t, e, n) {
    n(160),
    t.exports = n(0).Object.assign
}
, function(t, e, n) {
    var r = n(6);
    r(r.S + r.F, "Object", {
        assign: n(161)
    })
}
, function(t, e, n) {
    "use strict";
    var r = n(28)
      , o = n(54)
      , i = n(34)
      , a = n(33)
      , s = n(77)
      , u = Object.assign;
    t.exports = !u || n(21)(function() {
        var t = {}
          , e = {}
          , n = Symbol()
          , r = "abcdefghijklmnopqrst";
        return t[n] = 7,
        r.split("").forEach(function(t) {
            e[t] = t
        }),
        7 != u({}, t)[n] || Object.keys(u({}, e)).join("") != r
    }) ? function(t, e) {
        for (var n = a(t), u = arguments.length, c = 1, l = o.f, f = i.f; u > c; )
            for (var h, d = s(arguments[c++]), p = l ? r(d).concat(l(d)) : r(d), v = p.length, g = 0; v > g; )
                f.call(d, h = p[g++]) && (n[h] = d[h]);
        return n
    }
    : u
}
, function(t, e, n) {
    t.exports = {
        default: n(163),
        __esModule: !0
    }
}
, function(t, e, n) {
    n(164),
    t.exports = n(0).Object.keys
}
, function(t, e, n) {
    var r = n(33)
      , o = n(28);
    n(74)("keys", function() {
        return function(t) {
            return o(r(t))
        }
    })
}
, function(t, e, n) {
    n(51),
    n(166),
    t.exports = n(0).Array.from
}
, function(t, e, n) {
    "use strict";
    var r = n(20)
      , o = n(6)
      , i = n(33)
      , a = n(78)
      , s = n(79)
      , u = n(53)
      , c = n(167)
      , l = n(73);
    o(o.S + o.F * !n(80)(function(t) {
        Array.from(t)
    }), "Array", {
        from: function(t) {
            var e, n, o, f, h = i(t), d = "function" == typeof this ? this : Array, p = arguments.length, v = p > 1 ? arguments[1] : void 0, g = void 0 !== v, y = 0, m = l(h);
            if (g && (v = r(v, p > 2 ? arguments[2] : void 0, 2)),
            void 0 == m || d == Array && s(m))
                for (n = new d(e = u(h.length)); e > y; y++)
                    c(n, y, g ? v(h[y], y) : h[y]);
            else
                for (f = m.call(h),
                n = new d; !(o = f.next()).done; y++)
                    c(n, y, g ? a(f, v, [o.value, y], !0) : o.value);
            return n.length = y,
            n
        }
    })
}
, function(t, e, n) {
    "use strict";
    var r = n(8)
      , o = n(25);
    t.exports = function(t, e, n) {
        e in t ? r.f(t, e, o(0, n)) : t[e] = n
    }
}
, function(t, e, n) {
    "use strict";
    e.__esModule = !0;
    var r = function(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }(n(143));
    e.default = function(t) {
        if (Array.isArray(t)) {
            for (var e = 0, n = Array(t.length); e < t.length; e++)
                n[e] = t[e];
            return n
        }
        return (0,
        r.default)(t)
    }
}
, function(t, e, n) {
    "use strict";
    function r(t, e) {
        var n = {};
        for (var r in t)
            n[r] = {};
        for (var r in e)
            n[r] = {};
        return Object.keys(n).length
    }
    function o(t, e) {
        var n = 0;
        for (var r in t)
            void 0 !== e[r] && ++n;
        return n
    }
    function i(t, e, n, r) {
        var o = function(t, e) {
            var n = {}
              , r = function(t, e) {
                void 0 === n[t] && (n[t] = {}),
                n[t][e] = {}
            };
            return t.forEach(function(t) {
                var n = e.getSourceIndex(t)
                  , o = e.getTargetIndex(t);
                r(n, o),
                r(o, n)
            }),
            n
        }(t, r);
        t.forEach(function(t) {
            var i = o[r.getSourceIndex(t)]
              , a = o[r.getTargetIndex(t)];
            r.setLength(t, 1 + e * n(i, a))
        })
    }
    function a(t, e, n) {
        var r = []
          , o = 0
          , i = []
          , a = [];
        function s(t) {
            t.index = t.lowlink = o++,
            i.push(t),
            t.onStack = !0;
            for (var e = 0, n = t.out; e < n.length; e++) {
                var r = n[e];
                void 0 === r.index ? (s(r),
                t.lowlink = Math.min(t.lowlink, r.lowlink)) : r.onStack && (t.lowlink = Math.min(t.lowlink, r.index))
            }
            if (t.lowlink === t.index) {
                for (var u = []; i.length && ((r = i.pop()).onStack = !1,
                u.push(r),
                r !== t); )
                    ;
                a.push(u.map(function(t) {
                    return t.id
                }))
            }
        }
        for (var u = 0; u < t; u++)
            r.push({
                id: u,
                out: []
            });
        for (var c = 0, l = e; c < l.length; c++) {
            var f = l[c]
              , h = r[n.getSourceIndex(f)]
              , d = r[n.getTargetIndex(f)];
            h.out.push(d)
        }
        for (var p = 0, v = r; p < v.length; p++) {
            var g = v[p];
            void 0 === g.index && s(g)
        }
        return a
    }
    Object.defineProperty(e, "__esModule", {
        value: !0
    }),
    e.symmetricDiffLinkLengths = function(t, e, n) {
        void 0 === n && (n = 1),
        i(t, n, function(t, e) {
            return Math.sqrt(r(t, e) - o(t, e))
        }, e)
    }
    ,
    e.jaccardLinkLengths = function(t, e, n) {
        void 0 === n && (n = 1),
        i(t, n, function(t, e) {
            return Math.min(Object.keys(t).length, Object.keys(e).length) < 1.1 ? 0 : o(t, e) / r(t, e)
        }, e)
    }
    ,
    e.generateDirectedEdgeConstraints = function(t, e, n, r) {
        var o = {};
        a(t, e, r).forEach(function(t, e) {
            return t.forEach(function(t) {
                return o[t] = e
            })
        });
        var i = [];
        return e.forEach(function(t) {
            var e = r.getSourceIndex(t)
              , a = r.getTargetIndex(t);
            o[e] !== o[a] && i.push({
                axis: n,
                left: e,
                right: a,
                gap: r.getMinSeparation(t)
            })
        }),
        i
    }
    ,
    e.stronglyConnectedComponents = a
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = function() {
        function t() {
            this.locks = {}
        }
        return t.prototype.add = function(t, e) {
            this.locks[t] = e
        }
        ,
        t.prototype.clear = function() {
            this.locks = {}
        }
        ,
        t.prototype.isEmpty = function() {
            for (var t in this.locks)
                return !1;
            return !0
        }
        ,
        t.prototype.apply = function(t) {
            for (var e in this.locks)
                t(Number(e), this.locks[e])
        }
        ,
        t
    }();
    e.Locks = r;
    var o = function() {
        function t(t, e, n) {
            void 0 === n && (n = null),
            this.D = e,
            this.G = n,
            this.threshold = 1e-4,
            this.numGridSnapNodes = 0,
            this.snapGridSize = 100,
            this.snapStrength = 1e3,
            this.scaleSnapByMaxH = !1,
            this.random = new i,
            this.project = null,
            this.x = t,
            this.k = t.length;
            var o = this.n = t[0].length;
            this.H = new Array(this.k),
            this.g = new Array(this.k),
            this.Hd = new Array(this.k),
            this.a = new Array(this.k),
            this.b = new Array(this.k),
            this.c = new Array(this.k),
            this.d = new Array(this.k),
            this.e = new Array(this.k),
            this.ia = new Array(this.k),
            this.ib = new Array(this.k),
            this.xtmp = new Array(this.k),
            this.locks = new r,
            this.minD = Number.MAX_VALUE;
            for (var a, s = o; s--; )
                for (a = o; --a > s; ) {
                    var u = e[s][a];
                    u > 0 && u < this.minD && (this.minD = u)
                }
            for (this.minD === Number.MAX_VALUE && (this.minD = 1),
            s = this.k; s--; ) {
                for (this.g[s] = new Array(o),
                this.H[s] = new Array(o),
                a = o; a--; )
                    this.H[s][a] = new Array(o);
                this.Hd[s] = new Array(o),
                this.a[s] = new Array(o),
                this.b[s] = new Array(o),
                this.c[s] = new Array(o),
                this.d[s] = new Array(o),
                this.e[s] = new Array(o),
                this.ia[s] = new Array(o),
                this.ib[s] = new Array(o),
                this.xtmp[s] = new Array(o)
            }
        }
        return t.createSquareMatrix = function(t, e) {
            for (var n = new Array(t), r = 0; r < t; ++r) {
                n[r] = new Array(t);
                for (var o = 0; o < t; ++o)
                    n[r][o] = e(r, o)
            }
            return n
        }
        ,
        t.prototype.offsetDir = function() {
            for (var t = this, e = new Array(this.k), n = 0, r = 0; r < this.k; ++r) {
                var o = e[r] = this.random.getNextBetween(.01, 1) - .5;
                n += o * o
            }
            return n = Math.sqrt(n),
            e.map(function(e) {
                return e * (t.minD / n)
            })
        }
        ,
        t.prototype.computeDerivatives = function(t) {
            var e = this
              , n = this.n;
            if (!(n < 1)) {
                for (var r, o = new Array(this.k), i = new Array(this.k), a = new Array(this.k), s = 0, u = 0; u < n; ++u) {
                    for (r = 0; r < this.k; ++r)
                        a[r] = this.g[r][u] = 0;
                    for (var c = 0; c < n; ++c)
                        if (u !== c) {
                            for (var l = n; l--; ) {
                                var f = 0;
                                for (r = 0; r < this.k; ++r) {
                                    var h = o[r] = t[r][u] - t[r][c];
                                    f += i[r] = h * h
                                }
                                if (f > 1e-9)
                                    break;
                                var d = this.offsetDir();
                                for (r = 0; r < this.k; ++r)
                                    t[r][c] += d[r]
                            }
                            var p = Math.sqrt(f)
                              , v = this.D[u][c]
                              , g = null != this.G ? this.G[u][c] : 1;
                            if (g > 1 && p > v || !isFinite(v))
                                for (r = 0; r < this.k; ++r)
                                    this.H[r][u][c] = 0;
                            else {
                                g > 1 && (g = 1);
                                var y = v * v
                                  , m = 2 * g * (p - v) / (y * p)
                                  , _ = p * p * p
                                  , w = 2 * -g / (y * _);
                                for (isFinite(m) || console.log(m),
                                r = 0; r < this.k; ++r)
                                    this.g[r][u] += o[r] * m,
                                    a[r] -= this.H[r][u][c] = w * (_ + v * (i[r] - f) + p * f)
                            }
                        }
                    for (r = 0; r < this.k; ++r)
                        s = Math.max(s, this.H[r][u][u] = a[r])
                }
                var x = this.snapGridSize / 2
                  , b = this.snapGridSize
                  , k = this.snapStrength / (x * x)
                  , L = this.numGridSnapNodes;
                for (u = 0; u < L; ++u)
                    for (r = 0; r < this.k; ++r) {
                        var E = this.x[r][u]
                          , S = E / b
                          , N = S % 1
                          , T = S - N;
                        -x < (h = Math.abs(N) <= .5 ? E - T * b : E > 0 ? E - (T + 1) * b : E - (T - 1) * b) && h <= x && (this.scaleSnapByMaxH ? (this.g[r][u] += s * k * h,
                        this.H[r][u][u] += s * k) : (this.g[r][u] += k * h,
                        this.H[r][u][u] += k))
                    }
                this.locks.isEmpty() || this.locks.apply(function(n, o) {
                    for (r = 0; r < e.k; ++r)
                        e.H[r][n][n] += s,
                        e.g[r][n] -= s * (o[r] - t[r][n])
                })
            }
        }
        ,
        t.dotProd = function(t, e) {
            for (var n = 0, r = t.length; r--; )
                n += t[r] * e[r];
            return n
        }
        ,
        t.rightMultiply = function(e, n, r) {
            for (var o = e.length; o--; )
                r[o] = t.dotProd(e[o], n)
        }
        ,
        t.prototype.computeStepSize = function(e) {
            for (var n = 0, r = 0, o = 0; o < this.k; ++o)
                n += t.dotProd(this.g[o], e[o]),
                t.rightMultiply(this.H[o], e[o], this.Hd[o]),
                r += t.dotProd(e[o], this.Hd[o]);
            return 0 !== r && isFinite(r) ? 1 * n / r : 0
        }
        ,
        t.prototype.reduceStress = function() {
            this.computeDerivatives(this.x);
            for (var t = this.computeStepSize(this.g), e = 0; e < this.k; ++e)
                this.takeDescentStep(this.x[e], this.g[e], t);
            return this.computeStress()
        }
        ,
        t.copy = function(t, e) {
            for (var n = t.length, r = e[0].length, o = 0; o < n; ++o)
                for (var i = 0; i < r; ++i)
                    e[o][i] = t[o][i]
        }
        ,
        t.prototype.stepAndProject = function(e, n, r, o) {
            t.copy(e, n),
            this.takeDescentStep(n[0], r[0], o),
            this.project && this.project[0](e[0], e[1], n[0]),
            this.takeDescentStep(n[1], r[1], o),
            this.project && this.project[1](n[0], e[1], n[1]);
            for (var i = 2; i < this.k; i++)
                this.takeDescentStep(n[i], r[i], o)
        }
        ,
        t.mApply = function(t, e, n) {
            for (var r = t; r-- > 0; )
                for (var o = e; o-- > 0; )
                    n(r, o)
        }
        ,
        t.prototype.matrixApply = function(e) {
            t.mApply(this.k, this.n, e)
        }
        ,
        t.prototype.computeNextPosition = function(t, e) {
            var n = this;
            this.computeDerivatives(t);
            var r = this.computeStepSize(this.g);
            if (this.stepAndProject(t, e, this.g, r),
            this.project) {
                this.matrixApply(function(r, o) {
                    return n.e[r][o] = t[r][o] - e[r][o]
                });
                var o = this.computeStepSize(this.e);
                o = Math.max(.2, Math.min(o, 1)),
                this.stepAndProject(t, e, this.e, o)
            }
        }
        ,
        t.prototype.run = function(t) {
            for (var e = Number.MAX_VALUE, n = !1; !n && t-- > 0; ) {
                var r = this.rungeKutta();
                n = Math.abs(e / r - 1) < this.threshold,
                e = r
            }
            return e
        }
        ,
        t.prototype.rungeKutta = function() {
            var e = this;
            this.computeNextPosition(this.x, this.a),
            t.mid(this.x, this.a, this.ia),
            this.computeNextPosition(this.ia, this.b),
            t.mid(this.x, this.b, this.ib),
            this.computeNextPosition(this.ib, this.c),
            this.computeNextPosition(this.c, this.d);
            var n = 0;
            return this.matrixApply(function(t, r) {
                var o = (e.a[t][r] + 2 * e.b[t][r] + 2 * e.c[t][r] + e.d[t][r]) / 6
                  , i = e.x[t][r] - o;
                n += i * i,
                e.x[t][r] = o
            }),
            n
        }
        ,
        t.mid = function(e, n, r) {
            t.mApply(e.length, e[0].length, function(t, o) {
                return r[t][o] = e[t][o] + (n[t][o] - e[t][o]) / 2
            })
        }
        ,
        t.prototype.takeDescentStep = function(t, e, n) {
            for (var r = 0; r < this.n; ++r)
                t[r] = t[r] - n * e[r]
        }
        ,
        t.prototype.computeStress = function() {
            for (var t = 0, e = 0, n = this.n - 1; e < n; ++e)
                for (var r = e + 1, o = this.n; r < o; ++r) {
                    for (var i = 0, a = 0; a < this.k; ++a) {
                        var s = this.x[a][e] - this.x[a][r];
                        i += s * s
                    }
                    i = Math.sqrt(i);
                    var u = this.D[e][r];
                    if (isFinite(u)) {
                        var c = u - i;
                        t += c * c / (u * u)
                    }
                }
            return t
        }
        ,
        t.zeroDistance = 1e-10,
        t
    }();
    e.Descent = o;
    var i = function() {
        function t(t) {
            void 0 === t && (t = 1),
            this.seed = t,
            this.a = 214013,
            this.c = 2531011,
            this.m = 2147483648,
            this.range = 32767
        }
        return t.prototype.getNext = function() {
            return this.seed = (this.seed * this.a + this.c) % this.m,
            (this.seed >> 16) / this.range
        }
        ,
        t.prototype.getNextBetween = function(t, e) {
            return t + this.getNext() * (e - t)
        }
        ,
        t
    }();
    e.PseudoRandom = i
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = function() {
        function t(t) {
            this.scale = t,
            this.AB = 0,
            this.AD = 0,
            this.A2 = 0
        }
        return t.prototype.addVariable = function(t) {
            var e = this.scale / t.scale
              , n = t.offset / t.scale
              , r = t.weight;
            this.AB += r * e * n,
            this.AD += r * e * t.desiredPosition,
            this.A2 += r * e * e
        }
        ,
        t.prototype.getPosn = function() {
            return (this.AD - this.AB) / this.A2
        }
        ,
        t
    }();
    e.PositionStats = r;
    var o = function() {
        function t(t, e, n, r) {
            void 0 === r && (r = !1),
            this.left = t,
            this.right = e,
            this.gap = n,
            this.equality = r,
            this.active = !1,
            this.unsatisfiable = !1,
            this.left = t,
            this.right = e,
            this.gap = n,
            this.equality = r
        }
        return t.prototype.slack = function() {
            return this.unsatisfiable ? Number.MAX_VALUE : this.right.scale * this.right.position() - this.gap - this.left.scale * this.left.position()
        }
        ,
        t
    }();
    e.Constraint = o;
    var i = function() {
        function t(t, e, n) {
            void 0 === e && (e = 1),
            void 0 === n && (n = 1),
            this.desiredPosition = t,
            this.weight = e,
            this.scale = n,
            this.offset = 0
        }
        return t.prototype.dfdv = function() {
            return 2 * this.weight * (this.position() - this.desiredPosition)
        }
        ,
        t.prototype.position = function() {
            return (this.block.ps.scale * this.block.posn + this.offset) / this.scale
        }
        ,
        t.prototype.visitNeighbours = function(t, e) {
            var n = function(n, r) {
                return n.active && t !== r && e(n, r)
            };
            this.cOut.forEach(function(t) {
                return n(t, t.right)
            }),
            this.cIn.forEach(function(t) {
                return n(t, t.left)
            })
        }
        ,
        t
    }();
    e.Variable = i;
    var a = function() {
        function t(t) {
            this.vars = [],
            t.offset = 0,
            this.ps = new r(t.scale),
            this.addVariable(t)
        }
        return t.prototype.addVariable = function(t) {
            t.block = this,
            this.vars.push(t),
            this.ps.addVariable(t),
            this.posn = this.ps.getPosn()
        }
        ,
        t.prototype.updateWeightedPosition = function() {
            this.ps.AB = this.ps.AD = this.ps.A2 = 0;
            for (var t = 0, e = this.vars.length; t < e; ++t)
                this.ps.addVariable(this.vars[t]);
            this.posn = this.ps.getPosn()
        }
        ,
        t.prototype.compute_lm = function(t, e, n) {
            var r = this
              , o = t.dfdv();
            return t.visitNeighbours(e, function(e, i) {
                var a = r.compute_lm(i, t, n);
                i === e.right ? (o += a * e.left.scale,
                e.lm = a) : (o += a * e.right.scale,
                e.lm = -a),
                n(e)
            }),
            o / t.scale
        }
        ,
        t.prototype.populateSplitBlock = function(t, e) {
            var n = this;
            t.visitNeighbours(e, function(e, r) {
                r.offset = t.offset + (r === e.right ? e.gap : -e.gap),
                n.addVariable(r),
                n.populateSplitBlock(r, t)
            })
        }
        ,
        t.prototype.traverse = function(t, e, n, r) {
            var o = this;
            void 0 === n && (n = this.vars[0]),
            void 0 === r && (r = null),
            n.visitNeighbours(r, function(r, i) {
                e.push(t(r)),
                o.traverse(t, e, i, n)
            })
        }
        ,
        t.prototype.findMinLM = function() {
            var t = null;
            return this.compute_lm(this.vars[0], null, function(e) {
                !e.equality && (null === t || e.lm < t.lm) && (t = e)
            }),
            t
        }
        ,
        t.prototype.findMinLMBetween = function(t, e) {
            this.compute_lm(t, null, function() {});
            var n = null;
            return this.findPath(t, null, e, function(t, e) {
                !t.equality && t.right === e && (null === n || t.lm < n.lm) && (n = t)
            }),
            n
        }
        ,
        t.prototype.findPath = function(t, e, n, r) {
            var o = this
              , i = !1;
            return t.visitNeighbours(e, function(e, a) {
                i || a !== n && !o.findPath(a, t, n, r) || (i = !0,
                r(e, a))
            }),
            i
        }
        ,
        t.prototype.isActiveDirectedPathBetween = function(t, e) {
            if (t === e)
                return !0;
            for (var n = t.cOut.length; n--; ) {
                var r = t.cOut[n];
                if (r.active && this.isActiveDirectedPathBetween(r.right, e))
                    return !0
            }
            return !1
        }
        ,
        t.split = function(e) {
            return e.active = !1,
            [t.createSplitBlock(e.left), t.createSplitBlock(e.right)]
        }
        ,
        t.createSplitBlock = function(e) {
            var n = new t(e);
            return n.populateSplitBlock(e, null),
            n
        }
        ,
        t.prototype.splitBetween = function(e, n) {
            var r = this.findMinLMBetween(e, n);
            if (null !== r) {
                var o = t.split(r);
                return {
                    constraint: r,
                    lb: o[0],
                    rb: o[1]
                }
            }
            return null
        }
        ,
        t.prototype.mergeAcross = function(t, e, n) {
            e.active = !0;
            for (var r = 0, o = t.vars.length; r < o; ++r) {
                var i = t.vars[r];
                i.offset += n,
                this.addVariable(i)
            }
            this.posn = this.ps.getPosn()
        }
        ,
        t.prototype.cost = function() {
            for (var t = 0, e = this.vars.length; e--; ) {
                var n = this.vars[e]
                  , r = n.position() - n.desiredPosition;
                t += r * r * n.weight
            }
            return t
        }
        ,
        t
    }();
    e.Block = a;
    var s = function() {
        function t(t) {
            this.vs = t;
            var e = t.length;
            for (this.list = new Array(e); e--; ) {
                var n = new a(t[e]);
                this.list[e] = n,
                n.blockInd = e
            }
        }
        return t.prototype.cost = function() {
            for (var t = 0, e = this.list.length; e--; )
                t += this.list[e].cost();
            return t
        }
        ,
        t.prototype.insert = function(t) {
            t.blockInd = this.list.length,
            this.list.push(t)
        }
        ,
        t.prototype.remove = function(t) {
            var e = this.list.length - 1
              , n = this.list[e];
            this.list.length = e,
            t !== n && (this.list[t.blockInd] = n,
            n.blockInd = t.blockInd)
        }
        ,
        t.prototype.merge = function(t) {
            var e = t.left.block
              , n = t.right.block
              , r = t.right.offset - t.left.offset - t.gap;
            e.vars.length < n.vars.length ? (n.mergeAcross(e, t, r),
            this.remove(e)) : (e.mergeAcross(n, t, -r),
            this.remove(n))
        }
        ,
        t.prototype.forEach = function(t) {
            this.list.forEach(t)
        }
        ,
        t.prototype.updateBlockPositions = function() {
            this.list.forEach(function(t) {
                return t.updateWeightedPosition()
            })
        }
        ,
        t.prototype.split = function(t) {
            var e = this;
            this.updateBlockPositions(),
            this.list.forEach(function(n) {
                var r = n.findMinLM();
                null !== r && r.lm < u.LAGRANGIAN_TOLERANCE && (n = r.left.block,
                a.split(r).forEach(function(t) {
                    return e.insert(t)
                }),
                e.remove(n),
                t.push(r))
            })
        }
        ,
        t
    }();
    e.Blocks = s;
    var u = function() {
        function t(t, e) {
            this.vs = t,
            this.cs = e,
            this.vs = t,
            t.forEach(function(t) {
                t.cIn = [],
                t.cOut = []
            }),
            this.cs = e,
            e.forEach(function(t) {
                t.left.cOut.push(t),
                t.right.cIn.push(t)
            }),
            this.inactive = e.map(function(t) {
                return t.active = !1,
                t
            }),
            this.bs = null
        }
        return t.prototype.cost = function() {
            return this.bs.cost()
        }
        ,
        t.prototype.setStartingPositions = function(t) {
            this.inactive = this.cs.map(function(t) {
                return t.active = !1,
                t
            }),
            this.bs = new s(this.vs),
            this.bs.forEach(function(e, n) {
                return e.posn = t[n]
            })
        }
        ,
        t.prototype.setDesiredPositions = function(t) {
            this.vs.forEach(function(e, n) {
                return e.desiredPosition = t[n]
            })
        }
        ,
        t.prototype.mostViolated = function() {
            for (var e = Number.MAX_VALUE, n = null, r = this.inactive, o = r.length, i = o, a = 0; a < o; ++a) {
                var s = r[a];
                if (!s.unsatisfiable) {
                    var u = s.slack();
                    if ((s.equality || u < e) && (e = u,
                    n = s,
                    i = a,
                    s.equality))
                        break
                }
            }
            return i !== o && (e < t.ZERO_UPPERBOUND && !n.active || n.equality) && (r[i] = r[o - 1],
            r.length = o - 1),
            n
        }
        ,
        t.prototype.satisfy = function() {
            null == this.bs && (this.bs = new s(this.vs)),
            this.bs.split(this.inactive);
            for (var e = null; (e = this.mostViolated()) && (e.equality || e.slack() < t.ZERO_UPPERBOUND && !e.active); ) {
                var n = e.left.block;
                if (n !== e.right.block)
                    this.bs.merge(e);
                else {
                    if (n.isActiveDirectedPathBetween(e.right, e.left)) {
                        e.unsatisfiable = !0;
                        continue
                    }
                    var r = n.splitBetween(e.left, e.right);
                    if (null === r) {
                        e.unsatisfiable = !0;
                        continue
                    }
                    this.bs.insert(r.lb),
                    this.bs.insert(r.rb),
                    this.bs.remove(n),
                    this.inactive.push(r.constraint),
                    e.slack() >= 0 ? this.inactive.push(e) : this.bs.merge(e)
                }
            }
        }
        ,
        t.prototype.solve = function() {
            this.satisfy();
            for (var t = Number.MAX_VALUE, e = this.bs.cost(); Math.abs(t - e) > 1e-4; )
                this.satisfy(),
                t = e,
                e = this.bs.cost();
            return e
        }
        ,
        t.LAGRANGIAN_TOLERANCE = -1e-4,
        t.ZERO_UPPERBOUND = -1e-10,
        t
    }();
    e.Solver = u,
    e.removeOverlapInOneDimension = function(t, e, n) {
        for (var r = t.map(function(t) {
            return new i(t.desiredCenter)
        }), a = [], s = t.length, c = 0; c < s - 1; c++) {
            var l = t[c]
              , f = t[c + 1];
            a.push(new o(r[c],r[c + 1],(l.size + f.size) / 2))
        }
        var h = r[0]
          , d = r[s - 1]
          , p = t[0].size / 2
          , v = t[s - 1].size / 2
          , g = null
          , y = null;
        return e && (g = new i(e,1e3 * h.weight),
        r.push(g),
        a.push(new o(g,h,p))),
        n && (y = new i(n,1e3 * d.weight),
        r.push(y),
        a.push(new o(d,y,v))),
        new u(r,a).solve(),
        {
            newCenters: r.slice(0, t.length).map(function(t) {
                return t.position()
            }),
            lowerBound: g ? g.position() : h.position() - p,
            upperBound: y ? y.position() : d.position() + v
        }
    }
}
, function(t, e, n) {
    var r = n(173);
    "string" == typeof r && (r = [[t.i, r, ""]]);
    var o = {
        hmr: !0,
        transform: void 0,
        insertInto: void 0
    };
    n(31)(r, o);
    r.locals && (t.exports = r.locals)
}
, function(t, e, n) {
    (t.exports = n(30)(!1)).push([t.i, "body,\n* {\n  margin: 0;\n  padding: 0;\n  font-family: Helvetica Neue, Helvetica, Arial, sans-serif;\n  font-size: 14px;\n  box-sizing: border-box;\n}\nbody {\n  overflow: hidden;\n}\n.canvas-main {\n  width: 100vw;\n  height: 100vh;\n  cursor: pointer;\n}\na {\n  color: #0084ff;\n  cursor: pointer;\n  outline: none;\n  text-decoration: none;\n}\n.text-left {\n  text-align: left;\n}\n.w80 {\n  width: 80px;\n}\n.w50 {\n  width: 50px;\n}\ntable {\n  font-size: 14px;\n  border: 1px solid #eaf4ff;\n  width: 100%;\n  border-spacing: 0;\n}\ntable thead {\n  border: 0 solid #eaf4ff;\n  background: rgba(0, 132, 255, 0.03);\n  border-bottom-width: 1px;\n}\ntable th,\ntable td {\n  font-weight: normal;\n  border: 0 solid #eaf4ff;\n  border-left-width: 1px;\n  padding: 8px;\n  text-align: center;\n  border-bottom: 1px solid #eaf4ff;\n}\ntable th:first-child,\ntable td:first-child {\n  border-left-width: 0;\n}\n.graph-app-toolbar {\n  position: absolute;\n  right: 25pt;\n  bottom: 20pt;\n  color: #666666;\n  z-index: 20;\n}\n.graph-app-toolbar > ul {\n  background: #fff;\n  margin: 0px;\n  box-sizing: border-box;\n  margin-top: 8px;\n  text-align: center;\n  padding: 0px;\n  border: 0.5pt solid #E0E0E0;\n  border-radius: 5px;\n}\n.graph-app-toolbar .gpt {\n  font-size: 11pt;\n}\n.graph-app-toolbar hr {\n  border: 0;\n  height: 0.5pt;\n  background-image: linear-gradient(to right, rgba(0, 0, 0, 0), #dedede, rgba(0, 0, 0, 0));\n}\n.graph-app-toolbar ul > li {\n  padding-top: 7pt;\n  padding-bottom: 5.5pt;\n  width: 40pt;\n  list-style: none;\n}\n.graph-app-toolbar .toolbar-system {\n  color: #0084FF;\n}\n.graph-app-toolbar > ul > li > span {\n  font-size: 14pt;\n  display: block;\n  margin: 0 auto;\n}\n.graph-app-head {\n  background-color: #ffffff;\n  position: absolute;\n  width: 100%;\n  top: 0;\n  height: 44pt;\n  border-bottom: 1pt solid #E0E0E0;\n  display: none;\n}\n.graph-app-head .graph-app-info {\n  position: fixed;\n  display: inline-block;\n  height: 44pt;\n  line-height: 44pt;\n  left: 44pt;\n  font-size: 17pt;\n  color: #999999;\n  width: 500pt;\n}\n.graph-app-head .graph-app-current-node {\n  position: fixed;\n  display: inline-block;\n  line-height: 44pt;\n  font-size: 17pt;\n  color: #202020;\n  width: 400pt;\n}\n.graph-app-head .graph-app-link {\n  position: fixed;\n  display: inline-block;\n  line-height: 44pt;\n  font-size: 14pt;\n  color: #0084FF;\n  right: 25pt;\n}\n", ""])
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = y(n(36))
      , o = y(n(32))
      , i = y(n(16))
      , a = y(n(2))
      , s = y(n(4))
      , u = y(n(10))
      , c = y(n(11))
      , l = y(n(175))
      , f = n(12)
      , h = y(f)
      , d = n(35)
      , p = n(145)
      , v = n(177)
      , g = n(50);
    function y(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    var m = function(t) {
        function e(t) {
            (0,
            a.default)(this, e);
            var n = (0,
            u.default)(this, (e.__proto__ || (0,
            i.default)(e)).call(this));
            return n.state = {
                companyDetail: null,
                showNode: !1,
                showNav: "holder",
                filterStr: ""
            },
            n
        }
        return (0,
        c.default)(e, t),
        (0,
        s.default)(e, [{
            key: "changeFilterStr",
            value: function(t) {
                this.clearCompanyDetail(),
                this.setState({
                    filterStr: t.target.value
                })
            }
        }, {
            key: "toExtInfo",
            value: function(t, e) {
                var n = this.props.frameOption;
                n && window.parent != window && (2 == t.type ? window.parent.postMessage((0,
                o.default)({
                    action: "router_human",
                    nodeId: t.id,
                    cid: e,
                    nodeName: t.name,
                    _t: n.time
                }), n.origin) : window.parent.postMessage((0,
                o.default)({
                    action: "router_company",
                    nodeId: t.id,
                    _t: n.time
                }), n.origin))
            }
        }, {
            key: "toggleShowNodeState",
            value: function() {
                var t = this.state.showNode;
                this.setState({
                    showNode: !t,
                    companyDetail: null,
                    showNav: "holder",
                    filterStr: ""
                })
            }
        }, {
            key: "clearCompanyDetail",
            value: function() {
                this.setState({
                    companyDetail: null,
                    showNav: "holder"
                })
            }
        }, {
            key: "nodeEnter",
            value: function(t) {
                var e = this.props.canvas;
                e && e.mouseInNode(t)
            }
        }, {
            key: "nodeLeave",
            value: function(t) {
                var e = this.props.canvas;
                e && e.mouseLeaveNode(t)
            }
        }, {
            key: "focusNode",
            value: function(t) {
                var e = this.props.canvas;
                e && (e.focusNode(t),
                e.mouseInNode(t))
            }
        }, {
            key: "showNodeDetail",
            value: function(t) {
                var e = this;
                (0,
                g.company_getCompanyDiscoverLayout)(t).then(function(n) {
                    if ("ok" === n.state) {
                        e.nodeLeave(t);
                        var o = (0,
                        r.default)({}, n.data);
                        o.id = t,
                        e.setState({
                            companyDetail: o,
                            showNav: "holder",
                            showNode: !0
                        })
                    }
                })
            }
        }, {
            key: "componentWillReceiveProps",
            value: function(t) {
                t.companyDetail ? this.setState({
                    companyDetail: t.companyDetail,
                    showNode: !0,
                    showNav: "holder"
                }) : this.setState({
                    companyDetail: null,
                    showNav: "holder"
                })
            }
        }, {
            key: "filterShowNodeList",
            value: function() {
                var t = this.props.showNodes
                  , e = this.state.filterStr
                  , n = []
                  , o = (0,
                r.default)([], t)
                  , i = e;
                return i = (i = i || "").trim(),
                n.splice(0, n.length),
                o.forEach(function(t) {
                    var e = t.properties.name || t.properties.title;
                    ("" == i || e.indexOf(i) > -1) && n.push(t)
                }),
                n
            }
        }, {
            key: "renderExtInfo",
            value: function() {
                var t = this
                  , e = this.state
                  , n = e.showNav
                  , r = e.companyDetail;
                if ("holder" == n) {
                    var o = r.holder && r.holder.result ? r.holder.result : [];
                    return h.default.createElement("div", {
                        className: l.default.companyExtInfo
                    }, h.default.createElement("div", {
                        className: l.default.repeatScroller
                    }, h.default.createElement("div", {
                        className: l.default.repeatOffsetter
                    }, o.map(function(e, n) {
                        return h.default.createElement("div", {
                            key: n,
                            className: l.default.extInfoItem,
                            onClick: function() {
                                return t.toExtInfo(e, r.id)
                            }
                        }, e.name)
                    }))))
                }
                if ("invest" == n) {
                    var i = r.invest && r.invest.result ? r.invest.result : [];
                    return h.default.createElement("div", {
                        className: l.default.companyExtInfo
                    }, h.default.createElement("div", {
                        className: l.default.repeatScroller
                    }, h.default.createElement("div", {
                        className: l.default.repeatOffsetter
                    }, i.map(function(e, n) {
                        return h.default.createElement("div", {
                            key: n,
                            className: l.default.extInfoItem,
                            onClick: function() {
                                return t.toExtInfo(e, r.id)
                            }
                        }, e.name)
                    }))))
                }
                if ("staff" == n) {
                    var a = r.staff && r.staff.result ? r.staff.result : [];
                    return h.default.createElement("div", {
                        className: l.default.companyExtInfo
                    }, h.default.createElement("div", {
                        className: l.default.repeatScroller
                    }, h.default.createElement("div", {
                        className: l.default.repeatOffsetter
                    }, a.map(function(e, n) {
                        return h.default.createElement("div", {
                            key: n,
                            className: l.default.extInfoItem,
                            onClick: function() {
                                return t.toExtInfo(e, r.id)
                            }
                        }, e.name, "[", e.typeJoin[0], "]")
                    }))))
                }
                return h.default.createElement("div", null)
            }
        }, {
            key: "renderLegendMin",
            value: function() {
                var t = this
                  , e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : []
                  , n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : []
                  , r = this.state.showNode
                  , o = this.props
                  , i = o.toggleLinkType
                  , a = o.showLinkTypes;
                return h.default.createElement("div", {
                    className: l.default.legendMin
                }, h.default.createElement("div", {
                    className: l.default.legendSearch,
                    onClick: function() {
                        return t.toggleShowNodeState()
                    }
                }, h.default.createElement("i", {
                    className: l.default.tpp + " tpp " + (r ? "tpp-close" : "tpp-search") + "  " + l.default.searchBtn
                })), h.default.createElement("div", {
                    className: l.default.legendNode
                }, e.map(function(t, e) {
                    return h.default.createElement("div", {
                        key: e,
                        className: 0 != e ? l.default.nodeItem : ""
                    }, h.default.createElement("i", {
                        className: "tpp " + t.icon + " ",
                        style: {
                            color: t.color
                        }
                    }), h.default.createElement("div", {
                        className: l.default.nodeName
                    }, t.name), h.default.createElement("div", {
                        style: {
                            color: t.color
                        }
                    }, t.num))
                })), h.default.createElement("div", {
                    className: l.default.legendLink
                }, h.default.createElement("span", {
                    className: l.default.legendTitle
                }, "关系"), n.map(function(t, e) {
                    return h.default.createElement("div", {
                        key: e,
                        onClick: function() {
                            return i(t.code, a)
                        },
                        className: (0 != e ? l.default.linkItem : "") + " " + l.default.btnLinkItem
                    }, h.default.createElement("i", {
                        className: "tpp " + l.default.linkIcon + " " + ("" == t.color ? "tpp-square-o" : "tpp-check-square") + " ",
                        style: {
                            color: t.color
                        }
                    }), h.default.createElement("div", null, t.name))
                })))
            }
        }, {
            key: "renderLegendMax",
            value: function() {
                var t = this
                  , e = this
                  , n = this.props.util
                  , r = this.state
                  , o = r.showNode
                  , i = r.companyDetail
                  , a = r.showNav
                  , s = r.filterStr
                  , u = this.filterShowNodeList();
                if (!o)
                    return h.default.createElement("div", null);
                var c = void 0
                  , f = void 0;
                return i && i.properties && (c = (c = i.properties.regStatus || "").replace(/\(.*\)/g, "").replace(/（.*）/g, ""),
                f = n.dateFmt("yyyy-MM-dd", new Date(parseInt(i.properties.estiblishTime)))),
                h.default.createElement("div", {
                    className: l.default.legendMax
                }, h.default.createElement("div", {
                    className: l.default.searchWarp
                }, h.default.createElement("input", {
                    onChange: function(e) {
                        return t.changeFilterStr(e)
                    },
                    type: "text",
                    value: s
                })), i ? h.default.createElement("div", {
                    className: l.default.nodeInfoWarp
                }, h.default.createElement("div", {
                    className: l.default.companyTitle
                }, h.default.createElement("i", {
                    className: l.default.titleLeftIcon + " tpp tpp-angle-left",
                    onClick: function() {
                        return t.clearCompanyDetail()
                    }
                }), h.default.createElement("span", {
                    className: l.default.titleCompanyName,
                    onClick: function() {
                        return t.toExtInfo({
                            id: i.id,
                            type: 1
                        })
                    }
                }, i.properties.name), h.default.createElement("span", {
                    className: l.default.companyRegStatus
                }, c || "")), h.default.createElement("div", null, h.default.createElement("div", {
                    className: l.default.companyInfoItem
                }, "法人：", i.properties.legalPersonName), h.default.createElement("div", {
                    className: l.default.companyInfoItem
                }, "企业类型：", i.properties.companyOrgType), h.default.createElement("div", {
                    className: l.default.companyInfoItem
                }, "注册资本：", i.properties.regCapital), h.default.createElement("div", {
                    className: l.default.companyInfoItem
                }, "成立日期：", f), h.default.createElement("div", {
                    className: l.default.companyInfoItem
                }, "注册地址：", i.properties.regLocation)), h.default.createElement("div", null, h.default.createElement("div", {
                    className: l.default.companyExtNav
                }, h.default.createElement("div", {
                    className: l.default.extNavItem + " " + ("holder" == a ? l.default.active : ""),
                    onClick: function() {
                        return t.setState({
                            showNav: "holder"
                        })
                    }
                }, "股东信息", i.holder ? i.holder.total : 0), h.default.createElement("div", {
                    className: l.default.extNavItem + " " + ("invest" == a ? l.default.active : ""),
                    onClick: function() {
                        return t.setState({
                            showNav: "invest"
                        })
                    }
                }, "对外投资", i.invest ? i.invest.total : 0), h.default.createElement("div", {
                    className: l.default.extNavItem + " " + ("staff" == a ? l.default.active : ""),
                    onClick: function() {
                        return t.setState({
                            showNav: "staff"
                        })
                    }
                }, "主要人员", i.staff ? i.staff.total : 0)), this.renderExtInfo())) : h.default.createElement("div", {
                    className: l.default.nodeWarp
                }, h.default.createElement("div", {
                    className: l.default.repeatScroller
                }, h.default.createElement("div", {
                    className: l.default.repeatOffsetter
                }, u.map(function(t, n) {
                    return h.default.createElement("div", {
                        key: n,
                        className: l.default.repeatNodeItem,
                        onDoubleClick: function() {
                            return e.focusNode(t.id)
                        },
                        onMouseLeave: function() {
                            return e.nodeLeave(t.id)
                        },
                        onMouseEnter: function() {
                            return e.nodeEnter(t.id)
                        }
                    }, h.default.createElement("div", {
                        className: l.default.legendNodeName
                    }, t.properties.name), "Company" == t.labels[0] ? h.default.createElement("i", {
                        onClick: function() {
                            return e.showNodeDetail(t.id)
                        },
                        className: "tpp tpp-angle-right " + l.default.nodeRightIcon + " "
                    }) : h.default.createElement("div", null))
                })))))
            }
        }, {
            key: "render",
            value: function() {
                var t = this.props
                  , e = t.linkList
                  , n = t.nodeList;
                return void 0 === e && void 0 === n ? h.default.createElement("div", null) : h.default.createElement("div", {
                    className: l.default.graphLegends + " "
                }, h.default.createElement("div", null, this.renderLegendMin(n, e), this.renderLegendMax()))
            }
        }]),
        e
    }(f.Component);
    e.default = (0,
    d.connect)(function(t) {
        var e = {};
        return t.canvas && (e = function(t, e) {
            if (t.data) {
                var n = t.data
                  , o = []
                  , i = []
                  , a = (0,
                r.default)([], n.allLinkTypes)
                  , s = (0,
                r.default)([], n.showLinkTypes)
                  , u = (0,
                r.default)([], n.showNodes);
                a.forEach(function(t) {
                    var e = s.find(function(e) {
                        return e === t
                    });
                    o.push({
                        code: t,
                        name: p.LinkTypeMap[t].text,
                        color: e ? p.LinkTypeMap[t].color : ""
                    })
                });
                var c = 0
                  , l = 0;
                u.forEach(function(t) {
                    "human" == t.labels[0].toLowerCase() ? l++ : "company" == t.labels[0].toLowerCase() && c++
                }),
                c > 0 && i.push({
                    code: "company",
                    name: p.NodeTypeMap.company.text,
                    icon: p.NodeTypeMap.company.icon,
                    color: p.NodeTypeMap.company.color,
                    num: c,
                    className: ""
                }),
                l > 0 && i.push({
                    code: "human",
                    name: p.NodeTypeMap.human.text,
                    icon: p.NodeTypeMap.human.icon,
                    color: p.NodeTypeMap.human.color,
                    num: l,
                    className: ""
                }),
                e.linkList = o,
                e.nodeList = i,
                e.showLinkTypes = s,
                e.showNodes = u
            }
            return t.companyDetail && (e.companyDetail = t.companyDetail),
            t.canvas && (e.canvas = t.canvas),
            e
        }(t.canvas, e)),
        e
    }, function(t, e) {
        return {
            toggleLinkType: function(e, n) {
                t((0,
                v.toggleLinkType)(e, n))
            }
        }
    })(m)
}
, function(t, e, n) {
    var r = n(176);
    "string" == typeof r && (r = [[t.i, r, ""]]);
    var o = {
        hmr: !0,
        transform: void 0,
        insertInto: void 0
    };
    n(31)(r, o);
    r.locals && (t.exports = r.locals)
}
, function(t, e, n) {
    (e = t.exports = n(30)(!1)).push([t.i, ".LKo-qJn00Gaz9s_TVggAT {\n  position: absolute;\n  right: 6px;\n  top: 6px;\n}\n.LKo-qJn00Gaz9s_TVggAT ._1W_L4j2tyY2yqu2Qzx5Xy_ {\n  width: 40px;\n  text-align: center;\n}\n.LKo-qJn00Gaz9s_TVggAT ._2fO9qTDJhXUMo2wtxrZf8Y {\n  background: #ffffff;\n  border: 1px solid #ececec;\n  padding: 5px 0;\n  cursor: pointer;\n}\n.LKo-qJn00Gaz9s_TVggAT ._2fO9qTDJhXUMo2wtxrZf8Y ._3JSWC8wLUoex398W_06Jx0 {\n  cursor: pointer;\n  font-size: 16px;\n  font-weight: 100;\n}\n.LKo-qJn00Gaz9s_TVggAT ._1WgCe-7V_RJF4bWyQtyRQX {\n  cursor: pointer;\n  font-size: 16px;\n  font-weight: 100;\n}\n.LKo-qJn00Gaz9s_TVggAT .gTDndTKRH3HTKCcmTLcYT {\n  font-size: 14px;\n  padding: 10px 5px 5px 5px;\n  margin-top: 5px;\n  background: #ffffff;\n  border: 1px solid #ececec;\n}\n.LKo-qJn00Gaz9s_TVggAT .gTDndTKRH3HTKCcmTLcYT .dU-NBq0fsnAOYnxXuvPmw {\n  font-size: 18px;\n}\n.LKo-qJn00Gaz9s_TVggAT .gTDndTKRH3HTKCcmTLcYT ._2E8YL8zGxz5AgDjjYYfxtf {\n  margin-top: 5px;\n  border-top: 1px solid #ececec;\n  padding-top: 5px;\n}\n.LKo-qJn00Gaz9s_TVggAT .gTDndTKRH3HTKCcmTLcYT ._2aDTGUg7_TT6PL3R0lf3ix {\n  font-size: 14px;\n}\n.LKo-qJn00Gaz9s_TVggAT ._2YUHpIL6GlgvCJIyCkLYaP {\n  font-size: 14px;\n  margin-top: 5px;\n  background: #ffffff;\n  padding: 0 5px 10px 5px;\n  border: 1px solid #ececec;\n}\n.LKo-qJn00Gaz9s_TVggAT ._2YUHpIL6GlgvCJIyCkLYaP .oaZEgJtkyuugyEh1nGwuF {\n  margin: 0 -5px 5px;\n  border-bottom: 1px solid #ececec;\n  padding: 3px 0;\n  display: inline-block;\n}\n.LKo-qJn00Gaz9s_TVggAT ._2YUHpIL6GlgvCJIyCkLYaP ._3gbhlY8J9bWghRHc1f7bsH {\n  font-size: 18px;\n}\n.LKo-qJn00Gaz9s_TVggAT ._2YUHpIL6GlgvCJIyCkLYaP ._1E43Y6v569MW1YpgLfwPjs {\n  margin-top: 5px;\n  border-top: 1px solid #ececec;\n  padding-top: 5px;\n}\n.LKo-qJn00Gaz9s_TVggAT ._2YUHpIL6GlgvCJIyCkLYaP ._3dUGtqbTrK5RKm5hk3j1sc {\n  cursor: pointer;\n}\n.LKo-qJn00Gaz9s_TVggAT ._1rrokc2la60aexs4onn6Fs {\n  width: 246px;\n  position: absolute;\n  right: 39px;\n  top: 0px;\n}\n.LKo-qJn00Gaz9s_TVggAT ._1rPDDCc4dYAKxCAykby2ht {\n  height: 30px;\n  margin-bottom: 4px;\n  background: #fff;\n}\n.LKo-qJn00Gaz9s_TVggAT ._1rPDDCc4dYAKxCAykby2ht input {\n  width: 246px;\n  height: 30px;\n}\n.LKo-qJn00Gaz9s_TVggAT ._3r9dajbNvMk_9H5OlzBeNE {\n  width: 246px;\n  border: 1px solid #ebebeb;\n  height: calc(100vh - 260px);\n  background: #fff;\n  box-sizing: border-box;\n  display: block;\n  margin: 0;\n  overflow: hidden;\n  padding: 0;\n  position: relative;\n}\n.LKo-qJn00Gaz9s_TVggAT ._2uOkd476cwaYQWENz301y8 {\n  bottom: 0;\n  box-sizing: border-box;\n  left: 0;\n  margin: 0;\n  overflow-x: hidden;\n  padding: 0;\n  position: absolute;\n  right: 0;\n  top: 0;\n  -webkit-overflow-scrolling: touch;\n  overflow-y: auto;\n  height: 100%;\n}\n.LKo-qJn00Gaz9s_TVggAT ._3jaA1t48nIVwTqH5aiKinQ {\n  box-sizing: border-box;\n  left: 0;\n  margin: 0;\n  padding: 0;\n  position: relative;\n  right: 0;\n  top: 0;\n}\n.LKo-qJn00Gaz9s_TVggAT ._3nuB002kUqd5JJKLM8v7XR {\n  height: 30px;\n}\n.LKo-qJn00Gaz9s_TVggAT ._3nuB002kUqd5JJKLM8v7XR:hover {\n  background: #00a9be;\n  color: #fff;\n}\n.LKo-qJn00Gaz9s_TVggAT ._3vi4chPU6fTkHGgJiR1YTE {\n  display: inline-block;\n  margin: 0;\n  line-height: 14px;\n  padding: 7px 0 7px 14px;\n  font-size: 14px;\n  width: 200px;\n  text-overflow: ellipsis;\n  overflow: hidden;\n  word-break: keep-all;\n  white-space: nowrap;\n  cursor: pointer;\n  color: inherit;\n}\n.LKo-qJn00Gaz9s_TVggAT .IMWRmCnNy0WWvD9SjlgnY {\n  display: inline-block;\n  width: 20px;\n  height: 30px;\n  float: right;\n  padding-top: 5px;\n  color: inherit;\n  cursor: pointer;\n}\n.LKo-qJn00Gaz9s_TVggAT ._3DGvsbWJTookQx-C0ean6e {\n  background: #fff;\n  font-size: 14px;\n  padding: 10px 1px 0 10px;\n  border: 1px solid #ececec;\n}\n.LKo-qJn00Gaz9s_TVggAT ._2nC_YRQcZV94qkSQ3T8iK4 {\n  height: 45px;\n  line-height: 45px;\n  vertical-align: middle;\n  color: #171717;\n}\n.LKo-qJn00Gaz9s_TVggAT .NPja8i5hbb_HwcJXA9Luv {\n  float: left;\n  display: inline-block;\n  width: 10px;\n  height: 20px;\n  font-size: 16px;\n  cursor: pointer;\n  color: inherit;\n  margin-right: 4px;\n}\n.LKo-qJn00Gaz9s_TVggAT ._101Us_84ZEdYXGKcn59MV {\n  width: 180px;\n  overflow: hidden;\n  display: inline-block;\n  word-break: keep-all;\n  white-space: nowrap;\n  float: left;\n  text-overflow: ellipsis;\n  cursor: pointer;\n  color: inherit;\n}\n.LKo-qJn00Gaz9s_TVggAT ._2WC5OVUWg7gyO6i0zp2Dki {\n  border: 1px solid #00aae2;\n  color: #00aae2;\n  float: right;\n  height: 20px;\n  padding: 0;\n  margin: 10px 0 0;\n  line-height: 20px;\n}\n.LKo-qJn00Gaz9s_TVggAT .mZGvak-TZRBjWKAJ3Lyil {\n  font-size: 13px;\n  color: #777;\n  position: relative;\n}\n.LKo-qJn00Gaz9s_TVggAT ._14KX27ZoW8Z2fVcdRqQ9uF {\n  background: #f8f8f8;\n  margin: 0;\n  padding: 0;\n  overflow: hidden;\n}\n.LKo-qJn00Gaz9s_TVggAT ._22YY8G1nZuMUIvmgqF5aIh {\n  float: left;\n  width: 33%;\n  margin: 0;\n  padding: 0;\n  display: inline-block;\n  height: 38px;\n  line-height: 38px;\n  vertical-align: middle;\n  text-align: center;\n  border-top: 2px solid #d5d5d5;\n  white-space: nowrap;\n  font-size: 12px;\n  cursor: pointer;\n}\n.LKo-qJn00Gaz9s_TVggAT ._22YY8G1nZuMUIvmgqF5aIh._1r8iiecgFHu7cThBMKdCB1 {\n  border-top: 2px solid #00b2ca;\n  background: #fff;\n}\n.LKo-qJn00Gaz9s_TVggAT ._3uhGRY78jmbw5EYAEDuxTg {\n  height: calc(100vh - 515px);\n  box-sizing: border-box;\n  display: block;\n  margin: 0;\n  overflow: hidden;\n  padding: 0;\n  position: relative;\n}\n.LKo-qJn00Gaz9s_TVggAT ._1BR-pNprH43Kr9CJR_EOr4 {\n  line-height: 25px;\n  vertical-align: middle;\n  font-size: 13px;\n  cursor: pointer;\n}\n.LKo-qJn00Gaz9s_TVggAT ._1BR-pNprH43Kr9CJR_EOr4:hover {\n  color: #00a9be;\n}\n", ""]),
    e.locals = {
        graphLegends: "LKo-qJn00Gaz9s_TVggAT",
        legendMin: "_1W_L4j2tyY2yqu2Qzx5Xy_",
        legendSearch: "_2fO9qTDJhXUMo2wtxrZf8Y",
        fa: "_3JSWC8wLUoex398W_06Jx0",
        searchBtn: "_1WgCe-7V_RJF4bWyQtyRQX",
        legendNode: "gTDndTKRH3HTKCcmTLcYT",
        tpp: "dU-NBq0fsnAOYnxXuvPmw",
        nodeItem: "_2E8YL8zGxz5AgDjjYYfxtf",
        nodeName: "_2aDTGUg7_TT6PL3R0lf3ix",
        legendLink: "_2YUHpIL6GlgvCJIyCkLYaP",
        legendTitle: "oaZEgJtkyuugyEh1nGwuF",
        linkIcon: "_3gbhlY8J9bWghRHc1f7bsH",
        linkItem: "_1E43Y6v569MW1YpgLfwPjs",
        btnLinkItem: "_3dUGtqbTrK5RKm5hk3j1sc",
        legendMax: "_1rrokc2la60aexs4onn6Fs",
        searchWarp: "_1rPDDCc4dYAKxCAykby2ht",
        nodeWarp: "_3r9dajbNvMk_9H5OlzBeNE",
        repeatScroller: "_2uOkd476cwaYQWENz301y8",
        repeatOffsetter: "_3jaA1t48nIVwTqH5aiKinQ",
        repeatNodeItem: "_3nuB002kUqd5JJKLM8v7XR",
        legendNodeName: "_3vi4chPU6fTkHGgJiR1YTE",
        nodeRightIcon: "IMWRmCnNy0WWvD9SjlgnY",
        nodeInfoWarp: "_3DGvsbWJTookQx-C0ean6e",
        companyTitle: "_2nC_YRQcZV94qkSQ3T8iK4",
        titleLeftIcon: "NPja8i5hbb_HwcJXA9Luv",
        titleCompanyName: "_101Us_84ZEdYXGKcn59MV",
        companyRegStatus: "_2WC5OVUWg7gyO6i0zp2Dki",
        companyInfoItem: "mZGvak-TZRBjWKAJ3Lyil",
        companyExtNav: "_14KX27ZoW8Z2fVcdRqQ9uF",
        extNavItem: "_22YY8G1nZuMUIvmgqF5aIh",
        active: "_1r8iiecgFHu7cThBMKdCB1",
        companyExtInfo: "_3uhGRY78jmbw5EYAEDuxTg",
        extInfoItem: "_1BR-pNprH43Kr9CJR_EOr4"
    }
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = function(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }(n(36));
    e.toggleLinkType = function(t, e) {
        var n = {
            type: o.ACTION_TOGGLE_LINK_TYPE
        }
          , i = (0,
        r.default)([], e)
          , a = i.indexOf(t);
        if (-1 == a)
            i.push(t),
            n.data = i;
        else {
            if (1 == i.length)
                return n;
            i.splice(a, 1),
            n.data = i
        }
        return n
    }
    ,
    e.mouseInNode = function() {
        return {
            type: o.ACTION_MOUSE_IN_NODE
        }
    }
    ,
    e.mouseLeaveNode = function() {
        return {
            type: o.ACTION_MOUSE_LEAVENODE
        }
    }
    ;
    var o = n(146)
}
, , , , , , , , , , , function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = function(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }(n(36))
      , o = n(156);
    var i = {};
    e.default = function(t, e) {
        switch (t = t || i,
        e.type) {
        case o.ACTION_CURRENT_DETAIL:
            var n = (0,
            r.default)({}, t);
            return n.currentDetail = e.currentDetail,
            n;
        default:
            return t
        }
    }
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = s(n(168))
      , o = s(n(2))
      , i = s(n(4))
      , a = s(n(18));
    function s(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    var u = a.default.deepCopy
      , c = function() {
        function t(e, n, r) {
            (0,
            o.default)(this, t),
            this.clear(),
            this.pushNodes(e),
            this.pushLinks(n),
            this._dataStoreHistory = [],
            this.options = {}
        }
        return (0,
        i.default)(t, [{
            key: "clear",
            value: function() {
                this._nodes = [],
                this._links = [],
                this._paths = null,
                this._ids = [],
                this._allLinkTypes = [],
                this._idLinkCount = {},
                this._idLinkMax = null,
                this._nodeStore = {},
                this._linksStore = {},
                delete this._showLinkTypes,
                delete this._foundIds,
                delete this._filterNode,
                delete this._fromIds,
                delete this._allData,
                delete this._showPaths
            }
        }, {
            key: "pushNodes",
            value: function(t) {
                var e, n = this;
                if (t && t.length) {
                    var o = this.ids
                      , i = this.idName
                      , a = [];
                    t.forEach(function(t, e) {
                        -1 === o.findIndex(function(e) {
                            return String(t[i]) === String(e)
                        }) && o.push(t[i]),
                        n._nodeStore[t[i]] ? a.push(e) : n._nodeStore[t[i]] = t
                    }),
                    this.fuckNode(t, a),
                    (e = this._nodes).push.apply(e, (0,
                    r.default)(t))
                }
            }
        }, {
            key: "fuckNode",
            value: function(t, e) {
                for (var n = e.length; n--; )
                    t.splice(e[n], 1)
            }
        }, {
            key: "pushLinks",
            value: function(t) {
                var e, n = this;
                if (t && t.length) {
                    var o = this.sourceIdName
                      , i = this.targetIdName
                      , s = this.allLinkTypes
                      , u = this.idLinkCount;
                    this.idLinkMax = t[0][o],
                    t.forEach(function(t) {
                        var e = t[o]
                          , r = t[i];
                        t.source || (t.source = e,
                        t.target = r),
                        t.idSeq = a.default.idSeq(t.source, t.target),
                        t.type,
                        s.find(function(e) {
                            return t.type.toLowerCase() === e
                        }) || s.push(t.type.toLowerCase()),
                        u[e] || (u[e] = 0),
                        u[e]++,
                        u[n.idLinkMax] < u[e] && (n.idLinkMax = e),
                        u[r] || (u[r] = 0),
                        u[r]++,
                        u[n.idLinkMax] < u[r] && (n.idLinkMax = r),
                        n._linksStore[e] || (n._linksStore[e] = []),
                        n._linksStore[e].push(t),
                        n._linksStore[r] || (n._linksStore[r] = []),
                        n._linksStore[r].push(t)
                    }),
                    (e = this._links).push.apply(e, (0,
                    r.default)(t))
                }
            }
        }, {
            key: "getNode",
            value: function(t) {
                return this._nodeStore[t]
            }
        }, {
            key: "getLinks",
            value: function(t) {
                return this._linksStore[t]
            }
        }, {
            key: "record",
            value: function() {}
        }, {
            key: "addHistory",
            value: function(t) {
                t = t || {};
                var e = u(this, {});
                e.options = t,
                this._dataStoreHistory.push(e),
                this.historyLength > this.limit && this._dataStoreHistory.splice(1, this.historyLength - this.limit),
                this._step = this.historyLength
            }
        }, {
            key: "back",
            value: function() {
                this.isStart || this._step--;
                var t = this._dataStoreHistory[this._step - 1];
                t = u(t, {}),
                this._nodes = t._nodes,
                this._links = t._links,
                this._paths = t._paths,
                this._ids = t._ids,
                this._allLinkTypes = t._allLinkTypes,
                this._idLinkCount = t._idLinkCount,
                this._idLinkMax = t._idLinkMax,
                this._nodeStore = t._nodeStore,
                this._linksStore = t._linksStore,
                this._showLinkTypes = t._showLinkTypes,
                this._foundIds = t._foundIds,
                this.allData = t._allData,
                this.filterNode = t._filterNode
            }
        }, {
            key: "nodes",
            get: function() {
                return this._nodes
            }
        }, {
            key: "links",
            get: function() {
                return this._links
            }
        }, {
            key: "showNodes",
            get: function() {
                var t = this.showLinks
                  , e = this.showLinkTypes
                  , n = this.filterNode
                  , r = this
                  , o = [];
                return e.forEach(function(e) {
                    t.forEach(function(t) {
                        var i = t.type.toLowerCase()
                          , a = t.endNode
                          , s = t.startNode;
                        i === e && (-1 === o.findIndex(function(t) {
                            return String(a) === String(t.id)
                        }) && -1 === n.findIndex(function(t) {
                            return String(a) === String(t)
                        }) && o.push(r.getNode(a)),
                        -1 === o.findIndex(function(t) {
                            return String(s) === String(t.id)
                        }) && -1 === n.findIndex(function(t) {
                            return String(s) === String(t)
                        }) && o.push(r.getNode(s)))
                    })
                }),
                o
            }
        }, {
            key: "showLinks",
            get: function() {
                var t = this.links
                  , e = this.showLinkTypes
                  , n = this.filterNode
                  , r = this.showPaths
                  , o = [];
                r && r.forEach(function(t) {
                    t.active && (o = o.concat(t.relationships))
                });
                var i = [];
                return e.forEach(function(e) {
                    t.forEach(function(t) {
                        t.type.toLowerCase() === e && -1 === n.findIndex(function(e) {
                            return String(t.startNode) === String(e)
                        }) && -1 === n.findIndex(function(e) {
                            return String(t.endNode) === String(e)
                        }) && (r ? -1 != o.findIndex(function(e) {
                            return e.startNode === t.startNode && e.endNode === t.endNode || e.endNode === t.startNode && e.startNode === t.endNode
                        }) && i.push(t) : i.push(t))
                    })
                }),
                i
            }
        }, {
            key: "filterNode",
            get: function() {
                return this._filterNode || []
            },
            set: function(t) {
                if (t) {
                    this._filterNode = t;
                    var e = this.allData
                      , n = [];
                    for (var r in e)
                        e.hasOwnProperty(r) && "p_0" != r && r.indexOf("p_") > -1 && function() {
                            var o = e[r]
                              , i = o.nodes
                              , a = o.relationships
                              , s = i[0]
                              , u = i[i.length - 1];
                            -1 === t.findIndex(function(t) {
                                return String(s.id) === String(t) || String(u.id) === String(t)
                            }) && n.push({
                                pathLength: i.length - 1,
                                startNode: s,
                                endNode: u,
                                nodes: i,
                                expand: !1,
                                active: !0,
                                relationships: a
                            })
                        }();
                    this.showPaths = n
                }
            }
        }, {
            key: "showLinkTypes",
            get: function() {
                return this._showLinkTypes || this._allLinkTypes
            },
            set: function(t) {
                this._showLinkTypes = t
            }
        }, {
            key: "idLinkCount",
            get: function() {
                return this._idLinkCount || (this._idLinkCount = {}),
                this._idLinkCount
            }
        }, {
            key: "idLinkMax",
            get: function() {
                return this._idLinkMax
            },
            set: function(t) {
                this._idLinkMax = t
            }
        }, {
            key: "ids",
            get: function() {
                return this._ids || (this._ids = []),
                this._ids
            },
            set: function(t) {
                this._ids = t
            }
        }, {
            key: "foundIds",
            get: function() {
                return this._foundIds
            },
            set: function(t) {
                this._foundIds = t
            }
        }, {
            key: "allLinkTypes",
            get: function() {
                return this._allLinkTypes || (this._allLinkTypes = []),
                this._allLinkTypes
            }
        }, {
            key: "idName",
            get: function() {
                return this._idName || "id"
            },
            set: function(t) {
                t && (this._idName = t,
                this.clear())
            }
        }, {
            key: "sourceIdName",
            get: function() {
                return this._sourceIdName || "startNode"
            },
            set: function(t) {
                t && (this._sourceIdName = t,
                this.clear())
            }
        }, {
            key: "targetIdName",
            get: function() {
                return this._targetIdName || "endNode"
            },
            set: function(t) {
                t && (this._targetIdName = t,
                this.clear())
            }
        }, {
            key: "historyLength",
            get: function() {
                return this._dataStoreHistory.length
            }
        }, {
            key: "limit",
            get: function() {
                return this._limit || 5
            },
            set: function(t) {
                t && (this._limit = parseInt(t),
                this.historyLength > t && this._dataStoreHistory.splice(this.historyLength - t),
                this._step = this.historyLength)
            }
        }, {
            key: "step",
            get: function() {
                return this._step
            }
        }, {
            key: "isStart",
            get: function() {
                return 1 === this._step
            }
        }, {
            key: "isEnd",
            get: function() {
                return this._step === this.historyLength
            }
        }, {
            key: "fromIds",
            set: function(t) {
                this._fromIds = t
            },
            get: function() {
                return this._fromIds
            }
        }, {
            key: "coordinate",
            set: function(t) {
                this._coordinate = t
            },
            get: function() {
                return this._coordinate
            }
        }, {
            key: "allData",
            set: function(t) {
                this._allData = t;
                var e = [];
                for (var n in t)
                    if (t.hasOwnProperty(n) && "p_0" != n && n.indexOf("p_") > -1) {
                        var r = t[n]
                          , o = r.nodes
                          , i = r.relationships
                          , a = o[0]
                          , s = o[o.length - 1];
                        e.push({
                            pathLength: o.length - 1,
                            startNode: a,
                            endNode: s,
                            nodes: o,
                            expand: !1,
                            active: !0,
                            relationships: i
                        })
                    }
                this.showPaths = e
            },
            get: function() {
                return this._allData
            }
        }, {
            key: "showPaths",
            get: function() {
                return this._showPaths
            },
            set: function(t) {
                this._showPaths = t
            }
        }]),
        t
    }();
    e.default = c
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = function() {
        return function(t, e, n) {
            this.source = t,
            this.target = e,
            this.type = n
        }
    }();
    e.PowerEdge = r;
    var o = function() {
        function t(t, e, n, r) {
            var o = this;
            if (this.linkAccessor = n,
            this.modules = new Array(t),
            this.roots = [],
            r)
                this.initModulesFromGroup(r);
            else {
                this.roots.push(new s);
                for (var a = 0; a < t; ++a)
                    this.roots[0].add(this.modules[a] = new i(a))
            }
            this.R = e.length,
            e.forEach(function(t) {
                var e = o.modules[n.getSourceIndex(t)]
                  , r = o.modules[n.getTargetIndex(t)]
                  , i = n.getType(t);
                e.outgoing.add(i, r),
                r.incoming.add(i, e)
            })
        }
        return t.prototype.initModulesFromGroup = function(t) {
            var e = new s;
            this.roots.push(e);
            for (var n = 0; n < t.leaves.length; ++n) {
                var r = t.leaves[n]
                  , o = new i(r.id);
                this.modules[r.id] = o,
                e.add(o)
            }
            if (t.groups)
                for (var a = 0; a < t.groups.length; ++a) {
                    var c = t.groups[a]
                      , l = {};
                    for (var f in c)
                        "leaves" !== f && "groups" !== f && c.hasOwnProperty(f) && (l[f] = c[f]);
                    e.add(new i(-1 - a,new u,new u,this.initModulesFromGroup(c),l))
                }
            return e
        }
        ,
        t.prototype.merge = function(t, e, n) {
            void 0 === n && (n = 0);
            var r = t.incoming.intersection(e.incoming)
              , o = t.outgoing.intersection(e.outgoing)
              , a = new s;
            a.add(t),
            a.add(e);
            var u = new i(this.modules.length,o,r,a);
            this.modules.push(u);
            var c = function(n, r, o) {
                n.forAll(function(n, i) {
                    n.forAll(function(n) {
                        var a = n[r];
                        a.add(i, u),
                        a.remove(i, t),
                        a.remove(i, e),
                        t[o].remove(i, n),
                        e[o].remove(i, n)
                    })
                })
            };
            return c(o, "incoming", "outgoing"),
            c(r, "outgoing", "incoming"),
            this.R -= r.count() + o.count(),
            this.roots[n].remove(t),
            this.roots[n].remove(e),
            this.roots[n].add(u),
            u
        }
        ,
        t.prototype.rootMerges = function(t) {
            void 0 === t && (t = 0);
            for (var e = this.roots[t].modules(), n = e.length, r = new Array(n * (n - 1)), o = 0, i = 0, a = n - 1; i < a; ++i)
                for (var s = i + 1; s < n; ++s) {
                    var u = e[i]
                      , c = e[s];
                    r[o] = {
                        id: o,
                        nEdges: this.nEdges(u, c),
                        a: u,
                        b: c
                    },
                    o++
                }
            return r
        }
        ,
        t.prototype.greedyMerge = function() {
            for (var t = 0; t < this.roots.length; ++t)
                if (!(this.roots[t].modules().length < 2)) {
                    var e = this.rootMerges(t).sort(function(t, e) {
                        return t.nEdges == e.nEdges ? t.id - e.id : t.nEdges - e.nEdges
                    })[0];
                    if (!(e.nEdges >= this.R))
                        return this.merge(e.a, e.b, t),
                        !0
                }
        }
        ,
        t.prototype.nEdges = function(t, e) {
            var n = t.incoming.intersection(e.incoming)
              , r = t.outgoing.intersection(e.outgoing);
            return this.R - n.count() - r.count()
        }
        ,
        t.prototype.getGroupHierarchy = function(t) {
            var e = this
              , n = [];
            return function t(e, n, r) {
                e.forAll(function(e) {
                    if (e.isLeaf())
                        n.leaves || (n.leaves = []),
                        n.leaves.push(e.id);
                    else {
                        var o = n;
                        if (e.gid = r.length,
                        !e.isIsland() || e.isPredefined()) {
                            if (o = {
                                id: e.gid
                            },
                            e.isPredefined())
                                for (var i in e.definition)
                                    o[i] = e.definition[i];
                            n.groups || (n.groups = []),
                            n.groups.push(e.gid),
                            r.push(o)
                        }
                        t(e.children, o, r)
                    }
                })
            }(this.roots[0], {}, n),
            this.allEdges().forEach(function(o) {
                var i = e.modules[o.source]
                  , a = e.modules[o.target];
                t.push(new r(void 0 === i.gid ? o.source : n[i.gid],void 0 === a.gid ? o.target : n[a.gid],o.type))
            }),
            n
        }
        ,
        t.prototype.allEdges = function() {
            var e = [];
            return t.getEdges(this.roots[0], e),
            e
        }
        ,
        t.getEdges = function(e, n) {
            e.forAll(function(e) {
                e.getEdges(n),
                t.getEdges(e.children, n)
            })
        }
        ,
        t
    }();
    e.Configuration = o;
    var i = function() {
        function t(t, e, n, r, o) {
            void 0 === e && (e = new u),
            void 0 === n && (n = new u),
            void 0 === r && (r = new s),
            this.id = t,
            this.outgoing = e,
            this.incoming = n,
            this.children = r,
            this.definition = o
        }
        return t.prototype.getEdges = function(t) {
            var e = this;
            this.outgoing.forAll(function(n, o) {
                n.forAll(function(n) {
                    t.push(new r(e.id,n.id,o))
                })
            })
        }
        ,
        t.prototype.isLeaf = function() {
            return 0 === this.children.count()
        }
        ,
        t.prototype.isIsland = function() {
            return 0 === this.outgoing.count() && 0 === this.incoming.count()
        }
        ,
        t.prototype.isPredefined = function() {
            return void 0 !== this.definition
        }
        ,
        t
    }();
    function a(t, e) {
        var n = {};
        for (var r in t)
            r in e && (n[r] = t[r]);
        return n
    }
    e.Module = i;
    var s = function() {
        function t() {
            this.table = {}
        }
        return t.prototype.count = function() {
            return Object.keys(this.table).length
        }
        ,
        t.prototype.intersection = function(e) {
            var n = new t;
            return n.table = a(this.table, e.table),
            n
        }
        ,
        t.prototype.intersectionCount = function(t) {
            return this.intersection(t).count()
        }
        ,
        t.prototype.contains = function(t) {
            return t in this.table
        }
        ,
        t.prototype.add = function(t) {
            this.table[t.id] = t
        }
        ,
        t.prototype.remove = function(t) {
            delete this.table[t.id]
        }
        ,
        t.prototype.forAll = function(t) {
            for (var e in this.table)
                t(this.table[e])
        }
        ,
        t.prototype.modules = function() {
            var t = [];
            return this.forAll(function(e) {
                e.isPredefined() || t.push(e)
            }),
            t
        }
        ,
        t
    }();
    e.ModuleSet = s;
    var u = function() {
        function t() {
            this.sets = {},
            this.n = 0
        }
        return t.prototype.count = function() {
            return this.n
        }
        ,
        t.prototype.contains = function(t) {
            var e = !1;
            return this.forAllModules(function(n) {
                e || n.id != t || (e = !0)
            }),
            e
        }
        ,
        t.prototype.add = function(t, e) {
            (t in this.sets ? this.sets[t] : this.sets[t] = new s).add(e),
            ++this.n
        }
        ,
        t.prototype.remove = function(t, e) {
            var n = this.sets[t];
            n.remove(e),
            0 === n.count() && delete this.sets[t],
            --this.n
        }
        ,
        t.prototype.forAll = function(t) {
            for (var e in this.sets)
                t(this.sets[e], Number(e))
        }
        ,
        t.prototype.forAllModules = function(t) {
            this.forAll(function(e, n) {
                return e.forAll(t)
            })
        }
        ,
        t.prototype.intersection = function(e) {
            var n = new t;
            return this.forAll(function(t, r) {
                if (r in e.sets) {
                    var o = t.intersection(e.sets[r])
                      , i = o.count();
                    i > 0 && (n.sets[r] = o,
                    n.n += i)
                }
            }),
            n
        }
        ,
        t
    }();
    e.LinkSets = u,
    e.getGroups = function(t, e, n, r) {
        for (var i = t.length, a = new o(i,e,n,r); a.greedyMerge(); )
            ;
        var s = []
          , u = a.getGroupHierarchy(s);
        return s.forEach(function(e) {
            var n = function(n) {
                var r = e[n];
                "number" == typeof r && (e[n] = t[r])
            };
            n("source"),
            n("target")
        }),
        {
            groups: u,
            powerEdges: s
        }
    }
}
, function(t, e, n) {
    "use strict";
    var r = this && this.__extends || function() {
        var t = Object.setPrototypeOf || {
            __proto__: []
        }instanceof Array && function(t, e) {
            t.__proto__ = e
        }
        || function(t, e) {
            for (var n in e)
                e.hasOwnProperty(n) && (t[n] = e[n])
        }
        ;
        return function(e, n) {
            function r() {
                this.constructor = e
            }
            t(e, n),
            e.prototype = null === n ? Object.create(n) : (r.prototype = n.prototype,
            new r)
        }
    }();
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var o = function() {
        function t() {
            this.findIter = function(t) {
                for (var e = this._root, n = this.iterator(); null !== e; ) {
                    var r = this._comparator(t, e.data);
                    if (0 === r)
                        return n._cursor = e,
                        n;
                    n._ancestors.push(e),
                    e = e.get_child(r > 0)
                }
                return null
            }
        }
        return t.prototype.clear = function() {
            this._root = null,
            this.size = 0
        }
        ,
        t.prototype.find = function(t) {
            for (var e = this._root; null !== e; ) {
                var n = this._comparator(t, e.data);
                if (0 === n)
                    return e.data;
                e = e.get_child(n > 0)
            }
            return null
        }
        ,
        t.prototype.lowerBound = function(t) {
            return this._bound(t, this._comparator)
        }
        ,
        t.prototype.upperBound = function(t) {
            var e = this._comparator;
            return this._bound(t, function(t, n) {
                return e(n, t)
            })
        }
        ,
        t.prototype.min = function() {
            var t = this._root;
            if (null === t)
                return null;
            for (; null !== t.left; )
                t = t.left;
            return t.data
        }
        ,
        t.prototype.max = function() {
            var t = this._root;
            if (null === t)
                return null;
            for (; null !== t.right; )
                t = t.right;
            return t.data
        }
        ,
        t.prototype.iterator = function() {
            return new i(this)
        }
        ,
        t.prototype.each = function(t) {
            for (var e, n = this.iterator(); null !== (e = n.next()); )
                t(e)
        }
        ,
        t.prototype.reach = function(t) {
            for (var e, n = this.iterator(); null !== (e = n.prev()); )
                t(e)
        }
        ,
        t.prototype._bound = function(t, e) {
            for (var n = this._root, r = this.iterator(); null !== n; ) {
                var o = this._comparator(t, n.data);
                if (0 === o)
                    return r._cursor = n,
                    r;
                r._ancestors.push(n),
                n = n.get_child(o > 0)
            }
            for (var i = r._ancestors.length - 1; i >= 0; --i)
                if (e(t, (n = r._ancestors[i]).data) > 0)
                    return r._cursor = n,
                    r._ancestors.length = i,
                    r;
            return r._ancestors.length = 0,
            r
        }
        ,
        t
    }();
    e.TreeBase = o;
    var i = function() {
        function t(t) {
            this._tree = t,
            this._ancestors = [],
            this._cursor = null
        }
        return t.prototype.data = function() {
            return null !== this._cursor ? this._cursor.data : null
        }
        ,
        t.prototype.next = function() {
            if (null === this._cursor) {
                var t = this._tree._root;
                null !== t && this._minNode(t)
            } else {
                var e;
                if (null === this._cursor.right)
                    do {
                        if (e = this._cursor,
                        !this._ancestors.length) {
                            this._cursor = null;
                            break
                        }
                        this._cursor = this._ancestors.pop()
                    } while (this._cursor.right === e);
                else
                    this._ancestors.push(this._cursor),
                    this._minNode(this._cursor.right)
            }
            return null !== this._cursor ? this._cursor.data : null
        }
        ,
        t.prototype.prev = function() {
            if (null === this._cursor) {
                var t = this._tree._root;
                null !== t && this._maxNode(t)
            } else {
                var e;
                if (null === this._cursor.left)
                    do {
                        if (e = this._cursor,
                        !this._ancestors.length) {
                            this._cursor = null;
                            break
                        }
                        this._cursor = this._ancestors.pop()
                    } while (this._cursor.left === e);
                else
                    this._ancestors.push(this._cursor),
                    this._maxNode(this._cursor.left)
            }
            return null !== this._cursor ? this._cursor.data : null
        }
        ,
        t.prototype._minNode = function(t) {
            for (; null !== t.left; )
                this._ancestors.push(t),
                t = t.left;
            this._cursor = t
        }
        ,
        t.prototype._maxNode = function(t) {
            for (; null !== t.right; )
                this._ancestors.push(t),
                t = t.right;
            this._cursor = t
        }
        ,
        t
    }();
    e.Iterator = i;
    var a = function() {
        function t(t) {
            this.data = t,
            this.left = null,
            this.right = null,
            this.red = !0
        }
        return t.prototype.get_child = function(t) {
            return t ? this.right : this.left
        }
        ,
        t.prototype.set_child = function(t, e) {
            t ? this.right = e : this.left = e
        }
        ,
        t
    }()
      , s = function(t) {
        function e(e) {
            var n = t.call(this) || this;
            return n._root = null,
            n._comparator = e,
            n.size = 0,
            n
        }
        return r(e, t),
        e.prototype.insert = function(t) {
            var n = !1;
            if (null === this._root)
                this._root = new a(t),
                n = !0,
                this.size++;
            else {
                var r = new a(void 0)
                  , o = !1
                  , i = !1
                  , s = null
                  , u = r
                  , c = null
                  , l = this._root;
                for (u.right = this._root; ; ) {
                    if (null === l ? (l = new a(t),
                    c.set_child(o, l),
                    n = !0,
                    this.size++) : e.is_red(l.left) && e.is_red(l.right) && (l.red = !0,
                    l.left.red = !1,
                    l.right.red = !1),
                    e.is_red(l) && e.is_red(c)) {
                        var f = u.right === s;
                        l === c.get_child(i) ? u.set_child(f, e.single_rotate(s, !i)) : u.set_child(f, e.double_rotate(s, !i))
                    }
                    var h = this._comparator(l.data, t);
                    if (0 === h)
                        break;
                    i = o,
                    o = h < 0,
                    null !== s && (u = s),
                    s = c,
                    c = l,
                    l = l.get_child(o)
                }
                this._root = r.right
            }
            return this._root.red = !1,
            n
        }
        ,
        e.prototype.remove = function(t) {
            if (null === this._root)
                return !1;
            var n = new a(void 0)
              , r = n;
            r.right = this._root;
            for (var o = null, i = null, s = null, u = !0; null !== r.get_child(u); ) {
                var c = u;
                i = o,
                o = r,
                r = r.get_child(u);
                var l = this._comparator(t, r.data);
                if (u = l > 0,
                0 === l && (s = r),
                !e.is_red(r) && !e.is_red(r.get_child(u)))
                    if (e.is_red(r.get_child(!u))) {
                        var f = e.single_rotate(r, u);
                        o.set_child(c, f),
                        o = f
                    } else if (!e.is_red(r.get_child(!u))) {
                        var h = o.get_child(!c);
                        if (null !== h)
                            if (e.is_red(h.get_child(!c)) || e.is_red(h.get_child(c))) {
                                var d = i.right === o;
                                e.is_red(h.get_child(c)) ? i.set_child(d, e.double_rotate(o, c)) : e.is_red(h.get_child(!c)) && i.set_child(d, e.single_rotate(o, c));
                                var p = i.get_child(d);
                                p.red = !0,
                                r.red = !0,
                                p.left.red = !1,
                                p.right.red = !1
                            } else
                                o.red = !1,
                                h.red = !0,
                                r.red = !0
                    }
            }
            return null !== s && (s.data = r.data,
            o.set_child(o.right === r, r.get_child(null === r.left)),
            this.size--),
            this._root = n.right,
            null !== this._root && (this._root.red = !1),
            null !== s
        }
        ,
        e.is_red = function(t) {
            return null !== t && t.red
        }
        ,
        e.single_rotate = function(t, e) {
            var n = t.get_child(!e);
            return t.set_child(!e, n.get_child(e)),
            n.set_child(e, t),
            t.red = !0,
            n.red = !1,
            n
        }
        ,
        e.double_rotate = function(t, n) {
            return t.set_child(!n, e.single_rotate(t.get_child(!n), !n)),
            e.single_rotate(t, n)
        }
        ,
        e
    }(o);
    e.RBTree = s
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = function() {
        function t(t) {
            this.elem = t,
            this.subheaps = []
        }
        return t.prototype.toString = function(t) {
            for (var e = "", n = !1, r = 0; r < this.subheaps.length; ++r) {
                var o = this.subheaps[r];
                o.elem ? (n && (e += ","),
                e += o.toString(t),
                n = !0) : n = !1
            }
            return "" !== e && (e = "(" + e + ")"),
            (this.elem ? t(this.elem) : "") + e
        }
        ,
        t.prototype.forEach = function(t) {
            this.empty() || (t(this.elem, this),
            this.subheaps.forEach(function(e) {
                return e.forEach(t)
            }))
        }
        ,
        t.prototype.count = function() {
            return this.empty() ? 0 : 1 + this.subheaps.reduce(function(t, e) {
                return t + e.count()
            }, 0)
        }
        ,
        t.prototype.min = function() {
            return this.elem
        }
        ,
        t.prototype.empty = function() {
            return null == this.elem
        }
        ,
        t.prototype.contains = function(t) {
            if (this === t)
                return !0;
            for (var e = 0; e < this.subheaps.length; e++)
                if (this.subheaps[e].contains(t))
                    return !0;
            return !1
        }
        ,
        t.prototype.isHeap = function(t) {
            var e = this;
            return this.subheaps.every(function(n) {
                return t(e.elem, n.elem) && n.isHeap(t)
            })
        }
        ,
        t.prototype.insert = function(e, n) {
            return this.merge(new t(e), n)
        }
        ,
        t.prototype.merge = function(t, e) {
            return this.empty() ? t : t.empty() ? this : e(this.elem, t.elem) ? (this.subheaps.push(t),
            this) : (t.subheaps.push(this),
            t)
        }
        ,
        t.prototype.removeMin = function(t) {
            return this.empty() ? null : this.mergePairs(t)
        }
        ,
        t.prototype.mergePairs = function(e) {
            if (0 == this.subheaps.length)
                return new t(null);
            if (1 == this.subheaps.length)
                return this.subheaps[0];
            var n = this.subheaps.pop().merge(this.subheaps.pop(), e)
              , r = this.mergePairs(e);
            return n.merge(r, e)
        }
        ,
        t.prototype.decreaseKey = function(e, n, r, o) {
            var i = e.removeMin(o);
            e.elem = i.elem,
            e.subheaps = i.subheaps,
            null !== r && null !== i.elem && r(e.elem, e);
            var a = new t(n);
            return null !== r && r(n, a),
            this.merge(a, o)
        }
        ,
        t
    }();
    e.PairingHeap = r;
    var o = function() {
        function t(t) {
            this.lessThan = t
        }
        return t.prototype.top = function() {
            return this.empty() ? null : this.root.elem
        }
        ,
        t.prototype.push = function() {
            for (var t, e = [], n = 0; n < arguments.length; n++)
                e[n] = arguments[n];
            for (var o, i = 0; o = e[i]; ++i)
                t = new r(o),
                this.root = this.empty() ? t : this.root.merge(t, this.lessThan);
            return t
        }
        ,
        t.prototype.empty = function() {
            return !this.root || !this.root.elem
        }
        ,
        t.prototype.isHeap = function() {
            return this.root.isHeap(this.lessThan)
        }
        ,
        t.prototype.forEach = function(t) {
            this.root.forEach(t)
        }
        ,
        t.prototype.pop = function() {
            if (this.empty())
                return null;
            var t = this.root.min();
            return this.root = this.root.removeMin(this.lessThan),
            t
        }
        ,
        t.prototype.reduceKey = function(t, e, n) {
            void 0 === n && (n = null),
            this.root = this.root.decreaseKey(t, e, n, this.lessThan)
        }
        ,
        t.prototype.toString = function(t) {
            return this.root.toString(t)
        }
        ,
        t.prototype.count = function() {
            return this.root.count()
        }
        ,
        t
    }();
    e.PriorityQueue = o
}
, function(t, e, n) {
    "use strict";
    var r = this && this.__extends || function() {
        var t = Object.setPrototypeOf || {
            __proto__: []
        }instanceof Array && function(t, e) {
            t.__proto__ = e
        }
        || function(t, e) {
            for (var n in e)
                e.hasOwnProperty(n) && (t[n] = e[n])
        }
        ;
        return function(e, n) {
            function r() {
                this.constructor = e
            }
            t(e, n),
            e.prototype = null === n ? Object.create(n) : (r.prototype = n.prototype,
            new r)
        }
    }();
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var o = n(137)
      , i = function() {
        return function() {}
    }();
    e.Point = i;
    var a = function() {
        return function(t, e, n, r) {
            this.x1 = t,
            this.y1 = e,
            this.x2 = n,
            this.y2 = r
        }
    }();
    e.LineSegment = a;
    var s = function(t) {
        function e() {
            return null !== t && t.apply(this, arguments) || this
        }
        return r(e, t),
        e
    }(i);
    function u(t, e, n) {
        return (e.x - t.x) * (n.y - t.y) - (n.x - t.x) * (e.y - t.y)
    }
    function c(t, e, n) {
        return u(t, e, n) > 0
    }
    function l(t, e, n) {
        return u(t, e, n) < 0
    }
    function f(t, e) {
        var n = e.slice(0);
        return n.push(e[0]),
        {
            rtan: h(t, n),
            ltan: d(t, n)
        }
    }
    function h(t, e) {
        var n, r, o, i, a = e.length - 1;
        if (l(t, e[1], e[0]) && !c(t, e[a - 1], e[0]))
            return 0;
        for (n = 0,
        r = a; ; ) {
            if (r - n == 1)
                return c(t, e[n], e[r]) ? n : r;
            if ((i = l(t, e[(o = Math.floor((n + r) / 2)) + 1], e[o])) && !c(t, e[o - 1], e[o]))
                return o;
            c(t, e[n + 1], e[n]) ? i ? r = o : c(t, e[n], e[o]) ? r = o : n = o : i && l(t, e[n], e[o]) ? r = o : n = o
        }
    }
    function d(t, e) {
        var n, r, o, i, a = e.length - 1;
        if (c(t, e[a - 1], e[0]) && !l(t, e[1], e[0]))
            return 0;
        for (n = 0,
        r = a; ; ) {
            if (r - n == 1)
                return l(t, e[n], e[r]) ? n : r;
            if (i = l(t, e[(o = Math.floor((n + r) / 2)) + 1], e[o]),
            c(t, e[o - 1], e[o]) && !i)
                return o;
            l(t, e[n + 1], e[n]) ? i ? l(t, e[n], e[o]) ? r = o : n = o : r = o : i ? n = o : c(t, e[n], e[o]) ? r = o : n = o
        }
    }
    function p(t, e, n, r, o, i) {
        var a, s;
        s = r(t[a = n(e[0], t)], e);
        for (var u = !1; !u; ) {
            for (u = !0; a === t.length - 1 && (a = 0),
            !o(e[s], t[a], t[a + 1]); )
                ++a;
            for (; 0 === s && (s = e.length - 1),
            !i(t[a], e[s], e[s - 1]); )
                --s,
                u = !1
        }
        return {
            t1: a,
            t2: s
        }
    }
    function v(t, e) {
        return p(t, e, h, d, c, l)
    }
    e.PolyPoint = s,
    e.isLeft = u,
    e.ConvexHull = function(t) {
        var e, n = t.slice(0).sort(function(t, e) {
            return t.x !== e.x ? e.x - t.x : e.y - t.y
        }), r = t.length, o = n[0].x;
        for (e = 1; e < r && n[e].x === o; ++e)
            ;
        var i = e - 1
          , a = [];
        if (a.push(n[0]),
        i === r - 1)
            n[i].y !== n[0].y && a.push(n[i]);
        else {
            var s, c = r - 1, l = n[r - 1].x;
            for (e = r - 2; e >= 0 && n[e].x === l; e--)
                ;
            for (s = e + 1,
            e = i; ++e <= s; )
                if (!(u(n[0], n[s], n[e]) >= 0 && e < s)) {
                    for (; a.length > 1 && !(u(a[a.length - 2], a[a.length - 1], n[e]) > 0); )
                        a.length -= 1;
                    0 != e && a.push(n[e])
                }
            c != s && a.push(n[c]);
            var f = a.length;
            for (e = s; --e >= i; )
                if (!(u(n[c], n[i], n[e]) >= 0 && e > i)) {
                    for (; a.length > f && !(u(a[a.length - 2], a[a.length - 1], n[e]) > 0); )
                        a.length -= 1;
                    0 != e && a.push(n[e])
                }
        }
        return a
    }
    ,
    e.clockwiseRadialSweep = function(t, e, n) {
        e.slice(0).sort(function(e, n) {
            return Math.atan2(e.y - t.y, e.x - t.x) - Math.atan2(n.y - t.y, n.x - t.x)
        }).forEach(n)
    }
    ,
    e.tangent_PolyPolyC = p,
    e.LRtangent_PolyPolyC = function(t, e) {
        var n = v(e, t);
        return {
            t1: n.t2,
            t2: n.t1
        }
    }
    ,
    e.RLtangent_PolyPolyC = v,
    e.LLtangent_PolyPolyC = function(t, e) {
        return p(t, e, d, d, l, l)
    }
    ,
    e.RRtangent_PolyPolyC = function(t, e) {
        return p(t, e, h, h, c, c)
    }
    ;
    var g = function() {
        return function(t, e) {
            this.t1 = t,
            this.t2 = e
        }
    }();
    e.BiTangent = g;
    var y = function() {
        return function() {}
    }();
    e.BiTangents = y;
    var m = function(t) {
        function e() {
            return null !== t && t.apply(this, arguments) || this
        }
        return r(e, t),
        e
    }(i);
    e.TVGPoint = m;
    var _ = function() {
        return function(t, e, n, r) {
            this.id = t,
            this.polyid = e,
            this.polyvertid = n,
            this.p = r,
            r.vv = this
        }
    }();
    e.VisibilityVertex = _;
    var w = function() {
        function t(t, e) {
            this.source = t,
            this.target = e
        }
        return t.prototype.length = function() {
            var t = this.source.p.x - this.target.p.x
              , e = this.source.p.y - this.target.p.y;
            return Math.sqrt(t * t + e * e)
        }
        ,
        t
    }();
    e.VisibilityEdge = w;
    var x = function() {
        function t(t, e) {
            if (this.P = t,
            this.V = [],
            this.E = [],
            e)
                this.V = e.V.slice(0),
                this.E = e.E.slice(0);
            else {
                for (var n = t.length, r = 0; r < n; r++) {
                    for (var o = t[r], i = 0; i < o.length; ++i) {
                        var a = o[i]
                          , s = new _(this.V.length,r,i,a);
                        this.V.push(s),
                        i > 0 && this.E.push(new w(o[i - 1].vv,s))
                    }
                    o.length > 1 && this.E.push(new w(o[0].vv,o[o.length - 1].vv))
                }
                for (r = 0; r < n - 1; r++) {
                    var u = t[r];
                    for (i = r + 1; i < n; i++) {
                        var c = t[i]
                          , l = k(u, c);
                        for (var f in l) {
                            var h = l[f]
                              , d = u[h.t1]
                              , p = c[h.t2];
                            this.addEdgeIfVisible(d, p, r, i)
                        }
                    }
                }
            }
        }
        return t.prototype.addEdgeIfVisible = function(t, e, n, r) {
            this.intersectsPolys(new a(t.x,t.y,e.x,e.y), n, r) || this.E.push(new w(t.vv,e.vv))
        }
        ,
        t.prototype.addPoint = function(t, e) {
            var n = this.P.length;
            this.V.push(new _(this.V.length,n,0,t));
            for (var r = 0; r < n; ++r)
                if (r !== e) {
                    var o = this.P[r]
                      , i = f(t, o);
                    this.addEdgeIfVisible(t, o[i.ltan], e, r),
                    this.addEdgeIfVisible(t, o[i.rtan], e, r)
                }
            return t.vv
        }
        ,
        t.prototype.intersectsPolys = function(t, e, n) {
            for (var r = 0, o = this.P.length; r < o; ++r)
                if (r != e && r != n && b(t, this.P[r]).length > 0)
                    return !0;
            return !1
        }
        ,
        t
    }();
    function b(t, e) {
        for (var n = [], r = 1, i = e.length; r < i; ++r) {
            var a = o.Rectangle.lineIntersection(t.x1, t.y1, t.x2, t.y2, e[r - 1].x, e[r - 1].y, e[r].x, e[r].y);
            a && n.push(a)
        }
        return n
    }
    function k(t, e) {
        for (var n = t.length - 1, r = e.length - 1, o = new y, i = 0; i < n; ++i)
            for (var a = 0; a < r; ++a) {
                var s = t[0 == i ? n - 1 : i - 1]
                  , c = t[i]
                  , l = t[i + 1]
                  , f = e[0 == a ? r - 1 : a - 1]
                  , h = e[a]
                  , d = e[a + 1]
                  , p = u(s, c, h)
                  , v = u(c, f, h)
                  , m = u(c, h, d)
                  , _ = u(f, h, c)
                  , w = u(h, s, c)
                  , x = u(h, c, l);
                p >= 0 && v >= 0 && m < 0 && _ >= 0 && w >= 0 && x < 0 ? o.ll = new g(i,a) : p <= 0 && v <= 0 && m > 0 && _ <= 0 && w <= 0 && x > 0 ? o.rr = new g(i,a) : p <= 0 && v > 0 && m <= 0 && _ >= 0 && w < 0 && x >= 0 ? o.rl = new g(i,a) : p >= 0 && v < 0 && m >= 0 && _ <= 0 && w > 0 && x <= 0 && (o.lr = new g(i,a))
            }
        return o
    }
    function L(t, e) {
        return !t.every(function(t) {
            return !function(t, e) {
                for (var n = 1, r = e.length; n < r; ++n)
                    if (l(e[n - 1], e[n], t))
                        return !1;
                return !0
            }(t, e)
        })
    }
    e.TangentVisibilityGraph = x,
    e.tangents = k,
    e.polysOverlap = function(t, e) {
        if (L(t, e))
            return !0;
        if (L(e, t))
            return !0;
        for (var n = 1, r = t.length; n < r; ++n) {
            var o = t[n]
              , i = t[n - 1];
            if (b(new a(i.x,i.y,o.x,o.y), e).length > 0)
                return !0
        }
        return !1
    }
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = {
        PADDING: 10,
        GOLDEN_SECTION: (1 + Math.sqrt(5)) / 2,
        FLOAT_EPSILON: 1e-4,
        MAX_INERATIONS: 100
    };
    e.applyPacking = function(t, e, n, o, i) {
        void 0 === i && (i = 1);
        var a = 0
          , s = 0
          , u = e
          , c = n
          , l = (i = void 0 !== i ? i : 1,
        o = void 0 !== o ? o : 0,
        0)
          , f = 0
          , h = 0
          , d = 0
          , p = [];
        function v(t, e) {
            p = [],
            l = 0,
            f = 0,
            d = s;
            for (var n = 0; n < t.length; n++)
                g(t[n], e);
            return Math.abs(l / f - i)
        }
        function g(t, e) {
            for (var n = void 0, o = 0; o < p.length; o++)
                if (p[o].space_left >= t.height && p[o].x + p[o].width + t.width + r.PADDING - e <= r.FLOAT_EPSILON) {
                    n = p[o];
                    break
                }
            p.push(t),
            void 0 !== n ? (t.x = n.x + n.width + r.PADDING,
            t.y = n.bottom,
            t.space_left = t.height,
            t.bottom = t.y,
            n.space_left -= t.height + r.PADDING,
            n.bottom += t.height + r.PADDING) : (t.y = d,
            d += t.height + r.PADDING,
            t.x = a,
            t.bottom = t.y,
            t.space_left = t.height),
            t.y + t.height - f > -r.FLOAT_EPSILON && (f = t.y + t.height - s),
            t.x + t.width - l > -r.FLOAT_EPSILON && (l = t.x + t.width - a)
        }
        0 != t.length && (function(t) {
            t.forEach(function(t) {
                !function(t) {
                    var e = Number.MAX_VALUE
                      , n = Number.MAX_VALUE
                      , r = 0
                      , i = 0;
                    t.array.forEach(function(t) {
                        var a = void 0 !== t.width ? t.width : o
                          , s = void 0 !== t.height ? t.height : o;
                        a /= 2,
                        s /= 2,
                        r = Math.max(t.x + a, r),
                        e = Math.min(t.x - a, e),
                        i = Math.max(t.y + s, i),
                        n = Math.min(t.y - s, n)
                    }),
                    t.width = r - e,
                    t.height = i - n
                }(t)
            })
        }(t),
        function(t, e) {
            var n = Number.POSITIVE_INFINITY
              , o = 0;
            t.sort(function(t, e) {
                return e.height - t.height
            }),
            h = t.reduce(function(t, e) {
                return t.width < e.width ? t.width : e.width
            });
            for (var i = p = h, a = g = function(t) {
                var e = 0;
                return t.forEach(function(t) {
                    return e += t.width + r.PADDING
                }),
                e
            }(t), s = 0, u = Number.MAX_VALUE, c = Number.MAX_VALUE, l = -1, f = Number.MAX_VALUE, d = Number.MAX_VALUE; f > h || d > r.FLOAT_EPSILON; ) {
                if (1 != l)
                    var p = a - (a - i) / r.GOLDEN_SECTION
                      , u = v(t, p);
                if (0 != l)
                    var g = i + (a - i) / r.GOLDEN_SECTION
                      , c = v(t, g);
                if (f = Math.abs(p - g),
                d = Math.abs(u - c),
                u < n && (n = u,
                o = p),
                c < n && (n = c,
                o = g),
                u > c ? (i = p,
                p = g,
                u = c,
                l = 1) : (a = g,
                g = p,
                c = u,
                l = 0),
                s++ > 100)
                    break
            }
            v(t, o)
        }(t),
        function(t) {
            t.forEach(function(t) {
                var e = {
                    x: 0,
                    y: 0
                };
                t.array.forEach(function(t) {
                    e.x += t.x,
                    e.y += t.y
                }),
                e.x /= t.array.length,
                e.y /= t.array.length;
                var n = {
                    x: e.x - t.width / 2,
                    y: e.y - t.height / 2
                }
                  , r = {
                    x: t.x - n.x + u / 2 - l / 2,
                    y: t.y - n.y + c / 2 - f / 2
                };
                t.array.forEach(function(t) {
                    t.x += r.x,
                    t.y += r.y
                })
            })
        }(t))
    }
    ,
    e.separateGraphs = function(t, e) {
        for (var n = {}, r = {}, o = [], i = 0, a = 0; a < e.length; a++) {
            var s = e[a]
              , u = s.source
              , c = s.target;
            r[u.index] ? r[u.index].push(c) : r[u.index] = [c],
            r[c.index] ? r[c.index].push(u) : r[c.index] = [u]
        }
        for (a = 0; a < t.length; a++) {
            var l = t[a];
            n[l.index] || f(l, !0)
        }
        function f(t, e) {
            if (void 0 === n[t.index]) {
                e && (i++,
                o.push({
                    array: []
                })),
                n[t.index] = i,
                o[i - 1].array.push(t);
                var a = r[t.index];
                if (a)
                    for (var s = 0; s < a.length; s++)
                        f(a[s], !1)
            }
        }
        return o
    }
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = n(137)
      , o = n(171)
      , i = n(144)
      , a = function() {
        return function(t, e, n) {
            this.id = t,
            this.rect = e,
            this.children = n,
            this.leaf = void 0 === n || 0 === n.length
        }
    }();
    e.NodeWrapper = a;
    var s = function() {
        return function(t, e, n, r, o) {
            void 0 === r && (r = null),
            void 0 === o && (o = null),
            this.id = t,
            this.x = e,
            this.y = n,
            this.node = r,
            this.line = o
        }
    }();
    e.Vert = s;
    var u = function() {
        function t(e, n) {
            this.s = e,
            this.t = n;
            var r = t.findMatch(e, n)
              , o = n.slice(0).reverse()
              , i = t.findMatch(e, o);
            r.length >= i.length ? (this.length = r.length,
            this.si = r.si,
            this.ti = r.ti,
            this.reversed = !1) : (this.length = i.length,
            this.si = i.si,
            this.ti = n.length - i.ti - i.length,
            this.reversed = !0)
        }
        return t.findMatch = function(t, e) {
            for (var n = t.length, r = e.length, o = {
                length: 0,
                si: -1,
                ti: -1
            }, i = new Array(n), a = 0; a < n; a++) {
                i[a] = new Array(r);
                for (var s = 0; s < r; s++)
                    if (t[a] === e[s]) {
                        var u = i[a][s] = 0 === a || 0 === s ? 1 : i[a - 1][s - 1] + 1;
                        u > o.length && (o.length = u,
                        o.si = a - u + 1,
                        o.ti = s - u + 1)
                    } else
                        i[a][s] = 0
            }
            return o
        }
        ,
        t.prototype.getSequence = function() {
            return this.length >= 0 ? this.s.slice(this.si, this.si + this.length) : []
        }
        ,
        t
    }();
    e.LongestCommonSubsequence = u;
    var c = function() {
        function t(t, e, n) {
            void 0 === n && (n = 12);
            var o = this;
            this.originalnodes = t,
            this.groupPadding = n,
            this.leaves = null,
            this.nodes = t.map(function(t, n) {
                return new a(n,e.getBounds(t),e.getChildren(t))
            }),
            this.leaves = this.nodes.filter(function(t) {
                return t.leaf
            }),
            this.groups = this.nodes.filter(function(t) {
                return !t.leaf
            }),
            this.cols = this.getGridLines("x"),
            this.rows = this.getGridLines("y"),
            this.groups.forEach(function(t) {
                return t.children.forEach(function(e) {
                    return o.nodes[e].parent = t
                })
            }),
            this.root = {
                children: []
            },
            this.nodes.forEach(function(t) {
                void 0 === t.parent && (t.parent = o.root,
                o.root.children.push(t.id)),
                t.ports = []
            }),
            this.backToFront = this.nodes.slice(0),
            this.backToFront.sort(function(t, e) {
                return o.getDepth(t) - o.getDepth(e)
            }),
            this.backToFront.slice(0).reverse().filter(function(t) {
                return !t.leaf
            }).forEach(function(t) {
                var e = r.Rectangle.empty();
                t.children.forEach(function(t) {
                    return e = e.union(o.nodes[t].rect)
                }),
                t.rect = e.inflate(o.groupPadding)
            });
            var i = this.midPoints(this.cols.map(function(t) {
                return t.pos
            }))
              , u = this.midPoints(this.rows.map(function(t) {
                return t.pos
            }))
              , c = i[0]
              , l = i[i.length - 1]
              , f = u[0]
              , h = u[u.length - 1]
              , d = this.rows.map(function(t) {
                return {
                    x1: c,
                    x2: l,
                    y1: t.pos,
                    y2: t.pos
                }
            }).concat(u.map(function(t) {
                return {
                    x1: c,
                    x2: l,
                    y1: t,
                    y2: t
                }
            }))
              , p = this.cols.map(function(t) {
                return {
                    x1: t.pos,
                    x2: t.pos,
                    y1: f,
                    y2: h
                }
            }).concat(i.map(function(t) {
                return {
                    x1: t,
                    x2: t,
                    y1: f,
                    y2: h
                }
            }))
              , v = d.concat(p);
            v.forEach(function(t) {
                return t.verts = []
            }),
            this.verts = [],
            this.edges = [],
            d.forEach(function(t) {
                return p.forEach(function(e) {
                    var n = new s(o.verts.length,e.x1,t.y1);
                    t.verts.push(n),
                    e.verts.push(n),
                    o.verts.push(n);
                    for (var r = o.backToFront.length; r-- > 0; ) {
                        var i = o.backToFront[r]
                          , a = i.rect
                          , u = Math.abs(n.x - a.cx())
                          , c = Math.abs(n.y - a.cy());
                        if (u < a.width() / 2 && c < a.height() / 2) {
                            n.node = i;
                            break
                        }
                    }
                })
            }),
            v.forEach(function(t, e) {
                o.nodes.forEach(function(e, n) {
                    e.rect.lineIntersections(t.x1, t.y1, t.x2, t.y2).forEach(function(n, r) {
                        var i = new s(o.verts.length,n.x,n.y,e,t);
                        o.verts.push(i),
                        t.verts.push(i),
                        e.ports.push(i)
                    })
                });
                var n = Math.abs(t.y1 - t.y2) < .1
                  , r = function(t, e) {
                    return n ? e.x - t.x : e.y - t.y
                };
                t.verts.sort(r);
                for (var i = 1; i < t.verts.length; i++) {
                    var a = t.verts[i - 1]
                      , u = t.verts[i];
                    a.node && a.node === u.node && a.node.leaf || o.edges.push({
                        source: a.id,
                        target: u.id,
                        length: Math.abs(r(a, u))
                    })
                }
            })
        }
        return t.prototype.avg = function(t) {
            return t.reduce(function(t, e) {
                return t + e
            }) / t.length
        }
        ,
        t.prototype.getGridLines = function(t) {
            for (var e = [], n = this.leaves.slice(0, this.leaves.length); n.length > 0; ) {
                var r = n.filter(function(e) {
                    return e.rect["overlap" + t.toUpperCase()](n[0].rect)
                })
                  , o = {
                    nodes: r,
                    pos: this.avg(r.map(function(e) {
                        return e.rect["c" + t]()
                    }))
                };
                e.push(o),
                o.nodes.forEach(function(t) {
                    return n.splice(n.indexOf(t), 1)
                })
            }
            return e.sort(function(t, e) {
                return t.pos - e.pos
            }),
            e
        }
        ,
        t.prototype.getDepth = function(t) {
            for (var e = 0; t.parent !== this.root; )
                e++,
                t = t.parent;
            return e
        }
        ,
        t.prototype.midPoints = function(t) {
            for (var e = t[1] - t[0], n = [t[0] - e / 2], r = 1; r < t.length; r++)
                n.push((t[r] + t[r - 1]) / 2);
            return n.push(t[t.length - 1] + e / 2),
            n
        }
        ,
        t.prototype.findLineage = function(t) {
            var e = [t];
            do {
                t = t.parent,
                e.push(t)
            } while (t !== this.root);return e.reverse()
        }
        ,
        t.prototype.findAncestorPathBetween = function(t, e) {
            for (var n = this.findLineage(t), r = this.findLineage(e), o = 0; n[o] === r[o]; )
                o++;
            return {
                commonAncestor: n[o - 1],
                lineages: n.slice(o).concat(r.slice(o))
            }
        }
        ,
        t.prototype.siblingObstacles = function(t, e) {
            var n = this
              , r = this.findAncestorPathBetween(t, e)
              , o = {};
            r.lineages.forEach(function(t) {
                return o[t.id] = {}
            });
            var i = r.commonAncestor.children.filter(function(t) {
                return !(t in o)
            });
            return r.lineages.filter(function(t) {
                return t.parent !== r.commonAncestor
            }).forEach(function(t) {
                return i = i.concat(t.parent.children.filter(function(e) {
                    return e !== t.id
                }))
            }),
            i.map(function(t) {
                return n.nodes[t]
            })
        }
        ,
        t.getSegmentSets = function(t, e, n) {
            for (var r = [], o = 0; o < t.length; o++)
                for (var i = t[o], a = 0; a < i.length; a++) {
                    (f = i[a]).edgeid = o,
                    f.i = a;
                    var s = f[1][e] - f[0][e];
                    Math.abs(s) < .1 && r.push(f)
                }
            r.sort(function(t, n) {
                return t[0][e] - n[0][e]
            });
            for (var u = [], c = null, l = 0; l < r.length; l++) {
                var f = r[l];
                (!c || Math.abs(f[0][e] - c.pos) > .1) && (c = {
                    pos: f[0][e],
                    segments: []
                },
                u.push(c)),
                c.segments.push(f)
            }
            return u
        }
        ,
        t.nudgeSegs = function(t, e, n, r, i, a) {
            var s = r.length;
            if (!(s <= 1)) {
                for (var u = r.map(function(e) {
                    return new o.Variable(e[0][t])
                }), c = [], l = 0; l < s; l++)
                    for (var f = 0; f < s; f++)
                        if (l !== f) {
                            var h = r[l]
                              , d = r[f]
                              , p = h.edgeid
                              , v = d.edgeid
                              , g = -1
                              , y = -1;
                            "x" == t ? i(p, v) && (h[0][e] < h[1][e] ? (g = f,
                            y = l) : (g = l,
                            y = f)) : i(p, v) && (h[0][e] < h[1][e] ? (g = l,
                            y = f) : (g = f,
                            y = l)),
                            g >= 0 && c.push(new o.Constraint(u[g],u[y],a))
                        }
                new o.Solver(u,c).solve(),
                u.forEach(function(e, o) {
                    var i = r[o]
                      , a = e.position();
                    i[0][t] = i[1][t] = a;
                    var s = n[i.edgeid];
                    i.i > 0 && (s[i.i - 1][1][t] = a),
                    i.i < s.length - 1 && (s[i.i + 1][0][t] = a)
                })
            }
        }
        ,
        t.nudgeSegments = function(e, n, r, o, i) {
            for (var a = t.getSegmentSets(e, n, r), s = 0; s < a.length; s++) {
                for (var u = a[s], c = [], l = 0; l < u.segments.length; l++) {
                    var f = u.segments[l];
                    c.push({
                        type: 0,
                        s: f,
                        pos: Math.min(f[0][r], f[1][r])
                    }),
                    c.push({
                        type: 1,
                        s: f,
                        pos: Math.max(f[0][r], f[1][r])
                    })
                }
                c.sort(function(t, e) {
                    return t.pos - e.pos + t.type - e.type
                });
                var h = []
                  , d = 0;
                c.forEach(function(a) {
                    0 === a.type ? (h.push(a.s),
                    d++) : d--,
                    0 == d && (t.nudgeSegs(n, r, e, h, o, i),
                    h = [])
                })
            }
        }
        ,
        t.prototype.routeEdges = function(e, n, r, o) {
            var i = this
              , a = e.map(function(t) {
                return i.route(r(t), o(t))
            })
              , s = t.orderEdges(a)
              , u = a.map(function(e) {
                return t.makeSegments(e)
            });
            return t.nudgeSegments(u, "x", "y", s, n),
            t.nudgeSegments(u, "y", "x", s, n),
            t.unreverseEdges(u, a),
            u
        }
        ,
        t.unreverseEdges = function(t, e) {
            t.forEach(function(t, n) {
                e[n].reversed && (t.reverse(),
                t.forEach(function(t) {
                    t.reverse()
                }))
            })
        }
        ,
        t.angleBetween2Lines = function(t, e) {
            var n = Math.atan2(t[0].y - t[1].y, t[0].x - t[1].x)
              , r = Math.atan2(e[0].y - e[1].y, e[0].x - e[1].x)
              , o = n - r;
            return (o > Math.PI || o < -Math.PI) && (o = r - n),
            o
        }
        ,
        t.isLeft = function(t, e, n) {
            return (e.x - t.x) * (n.y - t.y) - (e.y - t.y) * (n.x - t.x) <= 0
        }
        ,
        t.getOrder = function(t) {
            for (var e = {}, n = 0; n < t.length; n++) {
                var r = t[n];
                void 0 === e[r.l] && (e[r.l] = {}),
                e[r.l][r.r] = !0
            }
            return function(t, n) {
                return void 0 !== e[t] && e[t][n]
            }
        }
        ,
        t.orderEdges = function(e) {
            for (var n = [], r = 0; r < e.length - 1; r++)
                for (var o = r + 1; o < e.length; o++) {
                    var i, a, s, c = e[r], l = e[o], f = new u(c,l);
                    0 !== f.length && (f.reversed && (l.reverse(),
                    l.reversed = !0,
                    f = new u(c,l)),
                    (f.si <= 0 || f.ti <= 0) && (f.si + f.length >= c.length || f.ti + f.length >= l.length) ? n.push({
                        l: r,
                        r: o
                    }) : (f.si + f.length >= c.length || f.ti + f.length >= l.length ? (i = c[f.si + 1],
                    s = c[f.si - 1],
                    a = l[f.ti - 1]) : (i = c[f.si + f.length - 2],
                    a = c[f.si + f.length],
                    s = l[f.ti + f.length]),
                    t.isLeft(i, a, s) ? n.push({
                        l: o,
                        r: r
                    }) : n.push({
                        l: r,
                        r: o
                    })))
                }
            return t.getOrder(n)
        }
        ,
        t.makeSegments = function(t) {
            function e(t) {
                return {
                    x: t.x,
                    y: t.y
                }
            }
            for (var n = function(t, e, n) {
                return Math.abs((e.x - t.x) * (n.y - t.y) - (e.y - t.y) * (n.x - t.x)) < .001
            }, r = [], o = e(t[0]), i = 1; i < t.length; i++) {
                var a = e(t[i])
                  , s = i < t.length - 1 ? t[i + 1] : null;
                s && n(o, a, s) || (r.push([o, a]),
                o = a)
            }
            return r
        }
        ,
        t.prototype.route = function(t, e) {
            var n = this
              , r = this.nodes[t]
              , o = this.nodes[e];
            this.obstacles = this.siblingObstacles(r, o);
            var a = {};
            this.obstacles.forEach(function(t) {
                return a[t.id] = t
            }),
            this.passableEdges = this.edges.filter(function(t) {
                var e = n.verts[t.source]
                  , r = n.verts[t.target];
                return !(e.node && e.node.id in a || r.node && r.node.id in a)
            });
            for (var s = 1; s < r.ports.length; s++) {
                var u = r.ports[0].id
                  , c = r.ports[s].id;
                this.passableEdges.push({
                    source: u,
                    target: c,
                    length: 0
                })
            }
            for (s = 1; s < o.ports.length; s++) {
                u = o.ports[0].id,
                c = o.ports[s].id;
                this.passableEdges.push({
                    source: u,
                    target: c,
                    length: 0
                })
            }
            var l = new i.Calculator(this.verts.length,this.passableEdges,function(t) {
                return t.source
            }
            ,function(t) {
                return t.target
            }
            ,function(t) {
                return t.length
            }
            ).PathFromNodeToNodeWithPrevCost(r.ports[0].id, o.ports[0].id, function(t, e, i) {
                var a = n.verts[t]
                  , s = n.verts[e]
                  , u = n.verts[i]
                  , c = Math.abs(u.x - a.x)
                  , l = Math.abs(u.y - a.y);
                return a.node === r && a.node === s.node || s.node === o && s.node === u.node ? 0 : c > 1 && l > 1 ? 1e3 : 0
            }).reverse().map(function(t) {
                return n.verts[t]
            });
            return l.push(this.nodes[o.id].ports[0]),
            l.filter(function(t, e) {
                return !(e < l.length - 1 && l[e + 1].node === r && t.node === r || e > 0 && t.node === o && l[e - 1].node === o)
            })
        }
        ,
        t.getRoutePath = function(e, n, r, o) {
            var i = {
                routepath: "M " + e[0][0].x + " " + e[0][0].y + " ",
                arrowpath: ""
            };
            if (e.length > 1)
                for (var a = 0; a < e.length; a++) {
                    var s = (w = e[a])[1].x
                      , u = w[1].y
                      , c = s - w[0].x
                      , l = u - w[0].y;
                    if (a < e.length - 1) {
                        Math.abs(c) > 0 ? s -= c / Math.abs(c) * n : u -= l / Math.abs(l) * n,
                        i.routepath += "L " + s + " " + u + " ";
                        var f = e[a + 1]
                          , h = f[0].x
                          , d = f[0].y;
                        c = f[1].x - h,
                        l = f[1].y - d;
                        var p, v, g = t.angleBetween2Lines(w, f) < 0 ? 1 : 0;
                        Math.abs(c) > 0 ? (p = h + c / Math.abs(c) * n,
                        v = d) : (p = h,
                        v = d + l / Math.abs(l) * n);
                        var y = Math.abs(p - s)
                          , m = Math.abs(v - u);
                        i.routepath += "A " + y + " " + m + " 0 0 " + g + " " + p + " " + v + " "
                    } else {
                        var _ = [s, u];
                        Math.abs(c) > 0 ? (x = [s -= c / Math.abs(c) * o, u + r],
                        b = [s, u - r]) : (x = [s + r, u -= l / Math.abs(l) * o],
                        b = [s - r, u]),
                        i.routepath += "L " + s + " " + u + " ",
                        o > 0 && (i.arrowpath = "M " + _[0] + " " + _[1] + " L " + x[0] + " " + x[1] + " L " + b[0] + " " + b[1])
                    }
                }
            else {
                var w, x, b;
                s = (w = e[0])[1].x,
                u = w[1].y,
                c = s - w[0].x,
                l = u - w[0].y,
                _ = [s, u];
                Math.abs(c) > 0 ? (x = [s -= c / Math.abs(c) * o, u + r],
                b = [s, u - r]) : (x = [s + r, u -= l / Math.abs(l) * o],
                b = [s - r, u]),
                i.routepath += "L " + s + " " + u + " ",
                o > 0 && (i.arrowpath = "M " + _[0] + " " + _[1] + " L " + x[0] + " " + x[1] + " L " + b[0] + " " + b[1])
            }
            return i
        }
        ,
        t
    }();
    e.GridRouter = c
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = h(n(16))
      , o = h(n(2))
      , i = h(n(4))
      , a = h(n(10))
      , s = h(n(11))
      , u = h(n(197))
      , c = n(12)
      , l = h(c)
      , f = n(35);
    function h(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    var d = function(t) {
        function e(t) {
            (0,
            o.default)(this, e);
            var n = (0,
            a.default)(this, (e.__proto__ || (0,
            r.default)(e)).call(this));
            return n.state = {
                show: !1,
                currentDetail: null,
                showTab: 1
            },
            n
        }
        return (0,
        s.default)(e, t),
        (0,
        i.default)(e, [{
            key: "componentWillReceiveProps",
            value: function(t) {
                t.currentDetail ? this.setState({
                    currentDetail: t.currentDetail,
                    show: !0,
                    showTab: 1
                }) : this.setState({
                    currentDetail: null,
                    show: !1,
                    showTab: 1
                })
            }
        }, {
            key: "renderListNull",
            value: function() {
                return l.default.createElement("tr", null, l.default.createElement("td", {
                    colSpan: 2,
                    className: u.default.dataNull
                }, l.default.createElement("img", {
                    className: u.default.dataNullImg,
                    src: "http://cdn.tianyancha.com/graph/resources/images/pop_null.png"
                }), "暂无信息"))
            }
        }, {
            key: "renderHolderList",
            value: function(t) {
                return t && t.length ? t.map(function(t, e) {
                    var n = void 0;
                    return "c" === t.type.toLowerCase() ? n = "https://www.tianyancha.com/company/" + t.id : "h" === t.type.toLowerCase() && (n = "https://www.tianyancha.com/human/" + t.id + "-c" + t.cid),
                    l.default.createElement("tr", {
                        key: e
                    }, l.default.createElement("td", {
                        className: "text-left"
                    }, l.default.createElement("a", {
                        href: n,
                        target: "_blank"
                    }, t.name)), l.default.createElement("td", null, t.percent ? t.percent : "-"))
                }) : this.renderListNull()
            }
        }, {
            key: "renderInverstList",
            value: function(t) {
                return t && t.length ? t.map(function(t, e) {
                    var n = "https://www.tianyancha.com/company/" + t.id;
                    return l.default.createElement("tr", {
                        key: e
                    }, l.default.createElement("td", {
                        className: "text-left"
                    }, l.default.createElement("a", {
                        href: n,
                        target: "_blank"
                    }, t.name)), l.default.createElement("td", null, t.percent ? t.percent : "-"))
                }) : this.renderListNull()
            }
        }, {
            key: "renderStaffList",
            value: function(t, e) {
                return t && t.length ? t.map(function(t, n) {
                    var r = void 0;
                    return 2 === t.type ? r = "https://www.tianyancha.com/human/" + t.id + "-c" + e : 1 === t.type && (r = "https://www.tianyancha.com/company/" + t.id),
                    l.default.createElement("tr", {
                        key: n
                    }, l.default.createElement("td", null, l.default.createElement("a", {
                        href: r,
                        target: "_blank"
                    }, t.name)), l.default.createElement("td", null, t.typeJoin ? t.typeJoin[0] : "-"))
                }) : this.renderListNull()
            }
        }, {
            key: "render",
            value: function() {
                var t = this
                  , e = this.state
                  , n = e.currentDetail
                  , r = e.show
                  , o = e.showTab;
                return n ? l.default.createElement("div", {
                    className: u.default.detail + " " + (r ? u.default.show : u.default.hide)
                }, l.default.createElement("div", {
                    className: u.default.header
                }, l.default.createElement("span", null, "公司信息"), l.default.createElement("i", {
                    className: u.default.close,
                    onClick: function() {
                        return t.setState({
                            show: !1
                        })
                    }
                }, "+")), l.default.createElement("div", {
                    className: u.default.content
                }, l.default.createElement("div", {
                    className: u.default.companyName
                }, l.default.createElement("div", {
                    className: u.default.title
                }, l.default.createElement("a", {
                    target: "_blank",
                    href: "https://www.tianyancha.com/company/" + n.baseInfo.id
                }, n.baseInfo.name)), l.default.createElement("div", {
                    className: u.default.tag
                }, n.baseInfo.regStatus)), l.default.createElement("div", {
                    className: u.default.info
                }, l.default.createElement("div", null, l.default.createElement("label", null, "法定代表人："), l.default.createElement("span", null, l.default.createElement("a", {
                    target: "_blank",
                    href: "https://www.tianyancha.com/human/" + n.baseInfo.legalPersonId + "-c" + n.baseInfo.id
                }, n.baseInfo.legal_person_name))), l.default.createElement("div", null, l.default.createElement("label", null, "法定资本："), l.default.createElement("span", null, n.baseInfo.reg_capital ? n.baseInfo.reg_capital : "-")), l.default.createElement("div", null, l.default.createElement("label", null, "成立时间："), l.default.createElement("span", null, n.baseInfo.estiblish_time ? n.baseInfo.estiblish_time : "-"))), l.default.createElement("div", {
                    className: u.default.tab
                }, l.default.createElement("div", {
                    className: u.default.tabHeader
                }, l.default.createElement("div", {
                    onClick: function() {
                        return t.setState({
                            showTab: 1
                        })
                    },
                    className: 1 === o ? u.default.active : ""
                }, "股东"), l.default.createElement("div", {
                    onClick: function() {
                        return t.setState({
                            showTab: 2
                        })
                    },
                    className: 2 === o ? u.default.active : ""
                }, "对外投资"), l.default.createElement("div", {
                    onClick: function() {
                        return t.setState({
                            showTab: 3
                        })
                    },
                    className: 3 === o ? u.default.active : ""
                }, "主要成员")), l.default.createElement("div", {
                    className: u.default.tabContent,
                    style: {
                        display: 1 === o ? "block" : "none"
                    }
                }, l.default.createElement("table", null, l.default.createElement("thead", null, l.default.createElement("tr", null, l.default.createElement("th", null, "企业名称/姓名"), l.default.createElement("th", {
                    className: "w50"
                }, "股比"))), l.default.createElement("tbody", null, this.renderHolderList(n.holderList)))), l.default.createElement("div", {
                    className: u.default.tabContent,
                    style: {
                        display: 2 === o ? "block" : "none"
                    }
                }, l.default.createElement("table", null, l.default.createElement("thead", null, l.default.createElement("tr", null, l.default.createElement("th", null, "企业名称"), l.default.createElement("th", {
                    className: "w50"
                }, "股比"))), l.default.createElement("tbody", null, this.renderInverstList(n.inverstList)))), l.default.createElement("div", {
                    className: u.default.tabContent,
                    style: {
                        display: 3 === o ? "block" : "none"
                    }
                }, l.default.createElement("table", null, l.default.createElement("thead", null, l.default.createElement("tr", null, l.default.createElement("th", null, "姓名"), l.default.createElement("th", {
                    className: "w50"
                }, "职务"))), l.default.createElement("tbody", null, this.renderStaffList(n.staffList, n.baseInfo.id))))))) : null
            }
        }]),
        e
    }(c.Component);
    e.default = (0,
    f.connect)(function(t) {
        return {
            currentDetail: t ? t.currentDetail : null
        }
    }, function(t, e) {
        return {}
    })(d)
}
, function(t, e, n) {
    var r = n(198);
    "string" == typeof r && (r = [[t.i, r, ""]]);
    var o = {
        hmr: !0,
        transform: void 0,
        insertInto: void 0
    };
    n(31)(r, o);
    r.locals && (t.exports = r.locals)
}
, function(t, e, n) {
    (e = t.exports = n(30)(!1)).push([t.i, "._3TBEN95gR0X_BIGUq5TuAS {\n  position: fixed;\n  left: 30px;\n  top: 60px;\n  width: 300px;\n  height: calc(100vh - 100px);\n  max-height: 576px;\n  color: #202020;\n  background: #ffffff;\n  box-shadow: 0 2px 6px 1px rgba(0, 0, 0, 0.32);\n  border-radius: 2px;\n  overflow-x: hidden;\n  overflow-y: auto;\n  animation-duration: 0.5s;\n  -webkit-animation-fill-mode: both;\n  animation-fill-mode: both;\n}\n@keyframes _3sFf2lsSs_y47rfr4_mneC {\n  from {\n    -webkit-transform: translate3d(-100%, 0, 0);\n    transform: translate3d(-100%, 0, 0);\n  }\n  to {\n    -webkit-transform: translate3d(0, 0, 0);\n    transform: translate3d(0, 0, 0);\n  }\n}\n@keyframes _1rTVYuFCVlih5TFpT9exdy {\n  from {\n    -webkit-transform: translate3d(0, 0, 0);\n    transform: translate3d(0, 0, 0);\n  }\n  to {\n    -webkit-transform: translate3d(-120%, 0, 0);\n    transform: translate3d(-120%, 0, 0);\n    display: none;\n  }\n}\n._3TBEN95gR0X_BIGUq5TuAS._1ZNTLukEpgVpWh0l_qHFUe {\n  animation-name: _1rTVYuFCVlih5TFpT9exdy;\n}\n._3TBEN95gR0X_BIGUq5TuAS._3Ou1OpoLEMjC2Ua6l8NZkf {\n  animation-name: _3sFf2lsSs_y47rfr4_mneC;\n}\n._3TBEN95gR0X_BIGUq5TuAS ._3EgscRE2FrqGnj4Pk3y3XY {\n  height: 40px;\n  font-size: 16px;\n  line-height: 40px;\n  vertical-align: middle;\n  text-align: center;\n  border: 0 solid #eaf4ff;\n  border-bottom-width: 1px;\n}\n._3TBEN95gR0X_BIGUq5TuAS ._1VvbyW2TekD3FXCvAy9DKd {\n  padding: 14px 20px 24px;\n}\n._3TBEN95gR0X_BIGUq5TuAS ._6hqdZwvMW_MLqQKzaag1U {\n  padding: 0 0 10px 0;\n  position: relative;\n  line-height: 28px;\n  font-size: 18px;\n}\n._3TBEN95gR0X_BIGUq5TuAS ._6hqdZwvMW_MLqQKzaag1U ._2NMGIHgmkFbOKFCJ1NDNlp {\n  word-break: break-all;\n}\n._3TBEN95gR0X_BIGUq5TuAS ._2JiBdB49XbpxwcnwQk0gq {\n  display: none;\n  position: absolute;\n  right: 0;\n  top: 0;\n  line-height: 26px;\n  font-size: 14px;\n  width: 40px;\n  border: 1px solid #34cc33;\n  word-break: keep-all;\n  white-space: nowrap;\n  overflow: hidden;\n  text-align: center;\n  border-radius: 2px;\n}\n._3TBEN95gR0X_BIGUq5TuAS ._14cViSHSmTxafpMBVcGuOv {\n  font-size: 14px;\n  line-height: 28px;\n  padding: 0 0 17px;\n}\n._3TBEN95gR0X_BIGUq5TuAS ._2ji8NkNngMOYPB_2gEYJMx {\n  display: flex;\n  align-items: flex-start;\n}\n._3TBEN95gR0X_BIGUq5TuAS ._2ji8NkNngMOYPB_2gEYJMx div {\n  font-size: 14px;\n  padding: 7px;\n  flex-grow: 1;\n  float: left;\n  text-align: center;\n  cursor: pointer;\n  border: 1px solid transparent;\n  border-bottom-width: 0;\n}\n._3TBEN95gR0X_BIGUq5TuAS ._2ji8NkNngMOYPB_2gEYJMx div:hover {\n  background: rgba(0, 132, 255, 0.03);\n}\n._3TBEN95gR0X_BIGUq5TuAS ._2ji8NkNngMOYPB_2gEYJMx div._3Et2eiAotAt_q0JnqY3PrR {\n  font-weight: bold;\n  border: 1px solid #eaf4ff;\n  border-bottom-width: 0;\n  color: #0084ff;\n}\n._3TBEN95gR0X_BIGUq5TuAS ._2WqOszycgv6sOCZRkeeDsh {\n  transform: rotate(45deg);\n  position: absolute;\n  right: 10px;\n  font-style: normal;\n  font-size: 32px;\n  cursor: pointer;\n}\n._3TBEN95gR0X_BIGUq5TuAS ._8p4SfOjJXqnsKjkJ_FXaj {\n  vertical-align: middle;\n  line-height: 94px;\n}\n._3TBEN95gR0X_BIGUq5TuAS ._12uqvMrd0bt6mrNzAnEw7w {\n  margin-bottom: -40px;\n  color: #737373;\n}\n", ""]),
    e.locals = {
        detail: "_3TBEN95gR0X_BIGUq5TuAS",
        hide: "_1ZNTLukEpgVpWh0l_qHFUe",
        slideOutLeft: "_1rTVYuFCVlih5TFpT9exdy",
        show: "_3Ou1OpoLEMjC2Ua6l8NZkf",
        slideInLeft: "_3sFf2lsSs_y47rfr4_mneC",
        header: "_3EgscRE2FrqGnj4Pk3y3XY",
        content: "_1VvbyW2TekD3FXCvAy9DKd",
        companyName: "_6hqdZwvMW_MLqQKzaag1U",
        title: "_2NMGIHgmkFbOKFCJ1NDNlp",
        tag: "_2JiBdB49XbpxwcnwQk0gq",
        info: "_14cViSHSmTxafpMBVcGuOv",
        tabHeader: "_2ji8NkNngMOYPB_2gEYJMx",
        active: "_3Et2eiAotAt_q0JnqY3PrR",
        close: "_2WqOszycgv6sOCZRkeeDsh",
        dataNull: "_8p4SfOjJXqnsKjkJ_FXaj",
        dataNullImg: "_12uqvMrd0bt6mrNzAnEw7w"
    }
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    }),
    e.currentDetail = function(t, e) {
        return function(e, n) {
            (0,
            o.loadCompanyDetail)(t).then(function(n) {
                e({
                    type: r.ACTION_CURRENT_DETAIL,
                    nodeId: t,
                    currentDetail: n.data
                })
            })
        }
    }
    ,
    e.currentDetailNull = function() {
        return {
            type: r.ACTION_CURRENT_DETAIL,
            currentDetail: null
        }
    }
    ;
    var r = n(156)
      , o = n(50)
}
, , , , , , , , , , function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = h(n(32))
      , o = h(n(143))
      , i = h(n(2))
      , a = h(n(4))
      , s = h(n(83))
      , u = h(n(37))
      , c = (h(n(52)),
    h(n(57)))
      , l = h(n(210))
      , f = h(n(18));
    function h(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    var d = u.default.Point
      , p = u.default.Layer
      , v = u.default.Shape
      , g = f.default.defScaleLinear
      , y = function() {
        function t(e, n) {
            if ((0,
            i.default)(this, t),
            n = n || {},
            this.canvas = "string" == typeof e ? document.querySelector(e) : e,
            !this.canvas)
                throw new TypeError(s.default.invalidCanvas);
            if (n.waterUrl && (this.waterUrl = n.waterUrl),
            n.service) {
                if (!n.service instanceof c.default)
                    throw new TypeError(s.default.invalidCanvas);
                this.service = n.service
            } else
                this.service = this.getService();
            n.host && (this.host = n.host),
            this.waterSize = n.waterSize || [350 * .7, 106 * .7],
            this.waterMargin = n.waterMargin || [160, 80],
            this.canvased(),
            this.canvasEvent()
        }
        return (0,
        a.default)(t, [{
            key: "getService",
            value: function() {
                return new c.default(this.host)
            }
        }, {
            key: "canvased",
            value: function() {
                var t = this
                  , e = this.canvas
                  , n = this.waterUrl
                  , r = this.waterSize;
                this.canvasPaper = new u.default.PaperScope,
                this.canvasPaper.setup(e),
                this.view = this.canvasPaper.view;
                var o = this.layerManager = new l.default(this.canvasPaper)
                  , i = this.canvasBlock = {
                    w: e.offsetWidth,
                    h: e.offsetHeight
                }
                  , a = this.canvasCenter = [e.offsetWidth / 2, e.offsetHeight / 2]
                  , s = this.waterLayer = new p;
                o.waterLayer = s;
                var c = this.waterRaster = new u.default.Raster({
                    crossOrigin: "anonymous",
                    source: n
                });
                c.size = new u.default.Size(r),
                c.on("load", function() {
                    var e = new u.default.Size(r);
                    this.setSize(e),
                    c.position = new d(a[0],a[1]),
                    t.drawWaterRaster()
                }),
                c.position = new d(a[0],a[1]),
                s.addChild(c),
                s.rotate(-20);
                var f = this.canvasLayer = new p;
                f.applyMatrix = !1,
                f.position = new d(0,0),
                f.pivot = new d(0,0),
                o.baseLayer = f,
                o.maskLayer = new p;
                var h = new v.Rectangle(0,0,i.w,i.h);
                h.fillColor = "white",
                h.opacity = .92,
                o.maskLayer.addChild(h),
                o.maskLayer.visible = !1;
                var g = new p;
                g.applyMatrix = !1,
                g.position = new d(0,0),
                g.pivot = new d(0,0),
                o.activeLayer = g
            }
        }, {
            key: "drawWaterRaster",
            value: function() {
                var t = this.waterLayer
                  , e = this.waterSize
                  , n = this.waterMargin
                  , r = this.canvas
                  , o = this.dataBlock
                  , i = this.scaleLinearX
                  , a = (this.scaleLinearY,
                this.viewScale,
                this.layerManager)
                  , s = this.canvasBlock
                  , u = o && o.w > s.w ? o.w : s.w
                  , c = o && o.h > s.h ? o.h : s.h;
                a.maskLayer.removeChildren();
                var l = new v.Rectangle(-u / 2 - 200,-c / 2 - 200,2 * u + 500,2 * c + 500);
                l.fillColor = "white",
                l.opacity = .92,
                a.maskLayer.addChild(l),
                t.removeChildren();
                var f = r.offsetWidth / 2;
                this.drawNextColumnWater(f);
                var h = r.offsetWidth
                  , d = 0;
                o.maxX && i(o.maxX) > h && (h = i(o.maxX)),
                o.minX && i(o.minX) < d && (d = i(o.minX));
                for (var p = !0; p; )
                    (f = f + e[0] + n[0]) < h + e[0] ? this.drawNextColumnWater(f, !1) : p = !1;
                for (p = !0,
                f = r.offsetWidth / 2; p; )
                    (f = f - e[0] - n[0]) > d - e[0] ? this.drawNextColumnWater(f, !1) : p = !1
            }
        }, {
            key: "drawNextColumnWater",
            value: function(t) {
                var e = this.waterLayer
                  , n = this.waterSize
                  , r = this.waterMargin
                  , o = this.canvas
                  , i = this.dataBlock
                  , a = (this.scaleLinearX,
                this.scaleLinearY)
                  , s = (this.viewScale,
                this.layerManager)
                  , c = o.offsetHeight / 2
                  , l = o.offsetHeight;
                i.maxY && a(i.maxY) > l && (l = a(i.maxY));
                var f = 0;
                i.minY && a(i.minY) < f && (f = a(i.minY));
                var h = this.waterRaster.clone();
                h.position = new d(t,c),
                h.size = new u.default.Size(n),
                e.addChild(h),
                (h = this.waterRaster.clone()).position = new d(t,c),
                h.size = new u.default.Size(n),
                h.opacity = .8,
                s.maskLayer.addChild(h);
                for (var p = !0; p; )
                    if ((c = c + n[1] + r[1]) < l + n[1]) {
                        var v = this.waterRaster.clone();
                        v.position = new d(t,c),
                        v.size = new u.default.Size(n),
                        e.addChild(v),
                        (v = this.waterRaster.clone()).position = new d(t,c),
                        v.size = new u.default.Size(n),
                        v.opacity = .8,
                        s.maskLayer.addChild(v)
                    } else
                        p = !1;
                for (p = !0,
                c = o.offsetHeight / 2; p; )
                    if ((c = c - n[1] - r[1]) > f - n[1]) {
                        var g = this.waterRaster.clone();
                        g.position = new d(t,c),
                        g.size = new u.default.Size(n),
                        e.addChild(g),
                        (g = this.waterRaster.clone()).position = new d(t,c),
                        g.size = new u.default.Size(n),
                        g.opacity = .8,
                        s.maskLayer.addChild(g)
                    } else
                        p = !1
            }
        }, {
            key: "canvasEvent",
            value: function() {
                this.view.onKeyDown = function(t) {
                    console.log(t)
                }
                ,
                this.view.minDistance = 10,
                this.view.onMouseDrag = function(t) {}
                ,
                this.view.onMouseMove = function(t) {}
            }
        }, {
            key: "errorHandler",
            value: function() {
                console && console.log && console.log.apply(null, (0,
                o.default)(arguments))
            }
        }, {
            key: "exportJSON",
            value: function() {
                this.drawWaterRaster();
                var t = this.canvasPaper.exportJSON({
                    asString: !0
                })
                  , e = JSON.parse(t);
                return e.projects[0] = null,
                String((0,
                r.default)(e))
            }
        }, {
            key: "size",
            value: function() {}
        }, {
            key: "host",
            get: function() {
                return this._host
            },
            set: function(t) {
                this._host = t
            }
        }, {
            key: "waterUrl",
            get: function() {
                return this._waterUrl || (this._waterUrl = "https://cdn.tianyancha.com/dis/resources/images/water_mark_new.png"),
                this._waterUrl
            },
            set: function(t) {
                this._waterUrl = t
            }
        }, {
            key: "scaleLinearX",
            get: function() {
                return g
            }
        }, {
            key: "scaleLinearY",
            get: function() {
                return g
            }
        }, {
            key: "viewScale",
            get: function() {
                return 1
            }
        }]),
        t
    }();
    e.default = y
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = i(n(2))
      , o = i(n(4));
    function i(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    var a = function() {
        function t(e) {
            (0,
            r.default)(this, t),
            this.paperScope = e
        }
        return (0,
        o.default)(t, [{
            key: "showMaskLayer",
            value: function(t) {
                var e = this.maskLayer;
                e && (e.visible = t,
                t || this.sendAllBackToBase())
            }
        }, {
            key: "sendToActive",
            value: function(t) {
                var e = this.baseLayer
                  , n = this.activeLayer;
                if (e && n) {
                    var r = e.children.findIndex(function(e) {
                        return e === t
                    });
                    r >= 0 && (e.removeChildren(r, r + 1),
                    n.addChild(t))
                }
            }
        }, {
            key: "sendAllBackToBase",
            value: function() {
                var t = this.baseLayer
                  , e = this.activeLayer;
                if (t && e)
                    for (; e.children && e.children.length > 0; ) {
                        var n = e.children[0];
                        e.removeChildren(0, 1),
                        t.addChild(n)
                    }
            }
        }, {
            key: "canvasLayerScale",
            value: function(t, e) {
                var n = this.baseLayer
                  , r = this.activeLayer;
                n && n.scale(t, e),
                r && r.scale(t, e)
            }
        }, {
            key: "canvasLayerTranslate",
            value: function(t) {
                var e = this.baseLayer
                  , n = this.activeLayer;
                e && e.translate(t),
                n && n.translate(t)
            }
        }, {
            key: "canvasLayerHitTest",
            value: function(t) {
                var e = this.baseLayer
                  , n = this.activeLayer;
                if (n) {
                    var r = n.hitTest(t);
                    if (r)
                        return r
                }
                if (e)
                    return e.hitTest(t)
            }
        }, {
            key: "canvasLayerRemoveAllChildren",
            value: function() {
                var t = this.baseLayer
                  , e = this.activeLayer;
                e && e.removeChildren(),
                t && t.removeChildren()
            }
        }, {
            key: "hitTestByLayer",
            value: function(t, e) {
                if (e)
                    return e.hitTest(t)
            }
        }, {
            key: "paperScope",
            set: function(t) {
                this._paperScope = t
            },
            get: function() {
                return this._paperScope
            }
        }, {
            key: "waterLayer",
            set: function(t) {
                this._waterLayer = t
            },
            get: function() {
                return this._waterLayer
            }
        }, {
            key: "baseLayer",
            set: function(t) {
                this._baseLayer = t
            },
            get: function() {
                return this._baseLayer
            }
        }, {
            key: "maskLayer",
            set: function(t) {
                this._maskLayer = t
            },
            get: function() {
                return this._maskLayer
            }
        }, {
            key: "activeLayer",
            set: function(t) {
                this._activeLayer = t
            },
            get: function() {
                return this._activeLayer
            }
        }]),
        t
    }();
    e.default = a
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    e.default = {
        node: {
            diameter: "40",
            visible: !0,
            "border-width": "1",
            color: "#DFE1E3",
            "border-color": "#0070D7",
            "font-color": "#FFFFFF",
            "font-size": "10",
            "hover-border-width": "12",
            "hover-border-color": "#FFFFFF"
        },
        "node.company": {
            diameter: "35",
            visible: !0,
            "border-width": "1",
            color: "#0183fe",
            "border-color": "#0070D7",
            "font-size": "12",
            "font-color": "#FFFFFF",
            "hover-border-width": "2",
            "hover-border-color": "#46a6ff",
            "hover-visible": !0,
            "hover-path-visible": !0,
            "hover-path-width": "6",
            "hover-path-color": "rgba(0,132,255,.46)"
        },
        "node.company.root": {
            diameter: "35",
            visible: !0,
            "border-width": "1",
            color: "#00b6c6",
            "border-color": "#008e9b",
            "font-size": "12",
            "font-color": "#FFFFFF",
            "hover-border-width": "2",
            "hover-border-color": "#00cee0",
            "hover-visible": !0,
            "hover-path-visible": !0,
            "hover-path-width": "6",
            "hover-path-color": "rgba(0,182,198,.46)"
        },
        "node.human": {
            visible: !0,
            diameter: "25",
            color: "#F25A29",
            "border-color": "#DC4717",
            "font-size": "12",
            "font-color": "#FFFFFF",
            "hover-border-width": "2",
            "hover-border-color": "#ff784d",
            "hover-visible": !0,
            "hover-path-visible": !0,
            "hover-path-width": "6",
            "hover-path-color": "rgba(242,90,42,.46)"
        },
        "node.human.root": {
            visible: !0,
            diameter: "25",
            color: "#00b6c6",
            "border-width": "1",
            "border-color": "#008e9b",
            "font-size": "12",
            "font-color": "#FFFFFF",
            "hover-border-width": "12",
            "hover-border-color": "rgba(0,182,198,.5)",
            "hover-visible": !0
        },
        "node.human.image": {
            visible: !0,
            diameter: "35",
            "border-width": "3",
            "border-color": "#f25a2a",
            "font-size": "12",
            "font-color": "#FFFFFF",
            "hover-border-width": "3",
            "hover-border-color": "#f25a2a",
            "hover-visible": !0,
            "hover-path-visible": !0,
            "hover-path-width": "6",
            "hover-path-color": "rgba(242,90,42,.46)"
        },
        relationship: {
            color: "#D4D6D7",
            "font-size": "10",
            "font-color": "#000000",
            "stroke-width": "1",
            "hover-font-size": "12",
            "hover-stroke-width": "2"
        },
        "relationship.invest": {
            color: "#f19d43",
            "font-size": "10",
            "font-color": "#000000",
            "stroke-width": "1",
            "hover-font-size": "12",
            "hover-stroke-width": "2"
        },
        "relationship.invest_c": {
            color: "#F25A29",
            "font-size": "10",
            "font-color": "#000000",
            "stroke-width": "1",
            "hover-font-size": "12",
            "hover-stroke-width": "2"
        },
        "relationship.invest_h": {
            color: "#F25A29",
            "font-size": "10",
            "font-color": "#000000",
            "stroke-width": "1",
            "hover-font-size": "12",
            "hover-stroke-width": "2"
        },
        "relationship.own": {
            color: "#cce198",
            "font-size": "10",
            "font-color": "#000000",
            "stroke-width": "1",
            "hover-color": "#00d0e3",
            "hover-font-size": "12",
            "hover-stroke-width": "2"
        },
        "relationship.branch": {
            color: "#91abd1",
            "font-size": "10",
            "font-color": "#000000",
            "stroke-width": "1",
            "hover-font-size": "12",
            "hover-color": "#0084ff",
            "hover-stroke-width": "2"
        },
        "relationship.serve": {
            color: "#80c2d8",
            "font-size": "10",
            "font-color": "#000000",
            "stroke-width": "1",
            "hover-font-size": "12",
            "hover-color": "#0084ff",
            "hover-stroke-width": "2"
        },
        "relationship.own_c": {
            color: "#cce198",
            "font-size": "10",
            "stroke-width": "1",
            "font-color": "#000000",
            "hover-font-size": "12",
            "hover-stroke-width": "2"
        }
    }
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = i(n(2))
      , o = i(n(4));
    function i(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    var a = function() {
        function t() {
            (0,
            r.default)(this, t),
            this.log = []
        }
        return (0,
        o.default)(t, [{
            key: "push",
            value: function(t) {
                this.log.push({
                    text: t,
                    time: Date.now()
                })
            }
        }, {
            key: "time_line",
            value: function() {
                return this.log.reduce(function(t, e) {
                    var n = t.value
                      , r = t.pre;
                    return null === r ? {
                        value: [],
                        pre: e
                    } : (n.push({
                        text: e.text,
                        time: e.time - r.time
                    }),
                    {
                        value: n,
                        pre: e
                    })
                }, {
                    value: [],
                    pre: null
                })
            }
        }, {
            key: "console",
            value: function(t) {
                function e() {
                    return t.apply(this, arguments)
                }
                return e.toString = function() {
                    return t.toString()
                }
                ,
                e
            }(function() {
                var t = this.time_line();
                console.log(t.value.map(function(t) {
                    return t.text + ":" + t.time + "\n"
                }).join(""))
            })
        }]),
        t
    }();
    e.default = a
}
, function(t, e, n) {
    "use strict";
    function r(t) {
        for (var n in t)
            e.hasOwnProperty(n) || (e[n] = t[n])
    }
    Object.defineProperty(e, "__esModule", {
        value: !0
    }),
    r(n(214)),
    r(n(215)),
    r(n(170)),
    r(n(193)),
    r(n(195)),
    r(n(194)),
    r(n(136)),
    r(n(218)),
    r(n(169)),
    r(n(190)),
    r(n(192)),
    r(n(191)),
    r(n(137)),
    r(n(144)),
    r(n(171)),
    r(n(219))
}
, function(t, e, n) {
    "use strict";
    var r = this && this.__extends || function() {
        var t = Object.setPrototypeOf || {
            __proto__: []
        }instanceof Array && function(t, e) {
            t.__proto__ = e
        }
        || function(t, e) {
            for (var n in e)
                e.hasOwnProperty(n) && (t[n] = e[n])
        }
        ;
        return function(e, n) {
            function r() {
                this.constructor = e
            }
            t(e, n),
            e.prototype = null === n ? Object.create(n) : (r.prototype = n.prototype,
            new r)
        }
    }();
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var o = n(136)
      , i = function(t) {
        function e(e) {
            var n = t.call(this) || this
              , r = e;
            return r.trigger && (n.trigger = r.trigger),
            r.kick && (n.kick = r.kick),
            r.drag && (n.drag = r.drag),
            r.on && (n.on = r.on),
            n.dragstart = n.dragStart = o.Layout.dragStart,
            n.dragend = n.dragEnd = o.Layout.dragEnd,
            n
        }
        return r(e, t),
        e.prototype.trigger = function(t) {}
        ,
        e.prototype.kick = function() {}
        ,
        e.prototype.drag = function() {}
        ,
        e.prototype.on = function(t, e) {
            return this
        }
        ,
        e
    }(o.Layout);
    e.LayoutAdaptor = i,
    e.adaptor = function(t) {
        return new i(t)
    }
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = n(216)
      , o = n(217);
    e.d3adaptor = function(t) {
        return !t || function(t) {
            return t.version && null !== t.version.match(/^3\./)
        }(t) ? new r.D3StyleLayoutAdaptor : new o.D3StyleLayoutAdaptor(t)
    }
}
, function(t, e, n) {
    "use strict";
    var r = this && this.__extends || function() {
        var t = Object.setPrototypeOf || {
            __proto__: []
        }instanceof Array && function(t, e) {
            t.__proto__ = e
        }
        || function(t, e) {
            for (var n in e)
                e.hasOwnProperty(n) && (t[n] = e[n])
        }
        ;
        return function(e, n) {
            function r() {
                this.constructor = e
            }
            t(e, n),
            e.prototype = null === n ? Object.create(n) : (r.prototype = n.prototype,
            new r)
        }
    }();
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var o = n(136)
      , i = function(t) {
        function e() {
            var e = t.call(this) || this;
            e.event = d3.dispatch(o.EventType[o.EventType.start], o.EventType[o.EventType.tick], o.EventType[o.EventType.end]);
            var n = e;
            return e.drag = function() {
                if (!t)
                    var t = d3.behavior.drag().origin(o.Layout.dragOrigin).on("dragstart.d3adaptor", o.Layout.dragStart).on("drag.d3adaptor", function(t) {
                        o.Layout.drag(t, d3.event),
                        n.resume()
                    }).on("dragend.d3adaptor", o.Layout.dragEnd);
                if (!arguments.length)
                    return t;
                this.call(t)
            }
            ,
            e
        }
        return r(e, t),
        e.prototype.trigger = function(t) {
            var e = {
                type: o.EventType[t.type],
                alpha: t.alpha,
                stress: t.stress
            };
            this.event[e.type](e)
        }
        ,
        e.prototype.kick = function() {
            var e = this;
            d3.timer(function() {
                return t.prototype.tick.call(e)
            })
        }
        ,
        e.prototype.on = function(t, e) {
            return "string" == typeof t ? this.event.on(t, e) : this.event.on(o.EventType[t], e),
            this
        }
        ,
        e
    }(o.Layout);
    e.D3StyleLayoutAdaptor = i,
    e.d3adaptor = function() {
        return new i
    }
}
, function(t, e, n) {
    "use strict";
    var r = this && this.__extends || function() {
        var t = Object.setPrototypeOf || {
            __proto__: []
        }instanceof Array && function(t, e) {
            t.__proto__ = e
        }
        || function(t, e) {
            for (var n in e)
                e.hasOwnProperty(n) && (t[n] = e[n])
        }
        ;
        return function(e, n) {
            function r() {
                this.constructor = e
            }
            t(e, n),
            e.prototype = null === n ? Object.create(n) : (r.prototype = n.prototype,
            new r)
        }
    }();
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var o = n(136)
      , i = function(t) {
        function e(e) {
            var n = t.call(this) || this;
            n.d3Context = e,
            n.event = e.dispatch(o.EventType[o.EventType.start], o.EventType[o.EventType.tick], o.EventType[o.EventType.end]);
            var r = n;
            return n.drag = function() {
                if (!t)
                    var t = e.drag().subject(o.Layout.dragOrigin).on("start.d3adaptor", o.Layout.dragStart).on("drag.d3adaptor", function(t) {
                        o.Layout.drag(t, e.event),
                        r.resume()
                    }).on("end.d3adaptor", o.Layout.dragEnd);
                if (!arguments.length)
                    return t;
                arguments[0].call(t)
            }
            ,
            n
        }
        return r(e, t),
        e.prototype.trigger = function(t) {
            var e = {
                type: o.EventType[t.type],
                alpha: t.alpha,
                stress: t.stress
            };
            this.event.call(e.type, e)
        }
        ,
        e.prototype.kick = function() {
            var e = this
              , n = this.d3Context.timer(function() {
                return t.prototype.tick.call(e) && n.stop()
            })
        }
        ,
        e.prototype.on = function(t, e) {
            return "string" == typeof t ? this.event.on(t, e) : this.event.on(o.EventType[t], e),
            this
        }
        ,
        e
    }(o.Layout);
    e.D3StyleLayoutAdaptor = i
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = n(144)
      , o = n(170)
      , i = n(137)
      , a = n(169)
      , s = function() {
        function t(t, e) {
            this.source = t,
            this.target = e
        }
        return t.prototype.actualLength = function(t) {
            var e = this;
            return Math.sqrt(t.reduce(function(t, n) {
                var r = n[e.target] - n[e.source];
                return t + r * r
            }, 0))
        }
        ,
        t
    }();
    e.Link3D = s;
    var u = function() {
        return function(t, e, n) {
            void 0 === t && (t = 0),
            void 0 === e && (e = 0),
            void 0 === n && (n = 0),
            this.x = t,
            this.y = e,
            this.z = n
        }
    }();
    e.Node3D = u;
    var c = function() {
        function t(e, n, r) {
            void 0 === r && (r = 1);
            var o = this;
            this.nodes = e,
            this.links = n,
            this.idealLinkLength = r,
            this.constraints = null,
            this.useJaccardLinkLengths = !0,
            this.result = new Array(t.k);
            for (var i = 0; i < t.k; ++i)
                this.result[i] = new Array(e.length);
            e.forEach(function(e, n) {
                for (var r = 0, i = t.dims; r < i.length; r++) {
                    var a = i[r];
                    void 0 === e[a] && (e[a] = Math.random())
                }
                o.result[0][n] = e.x,
                o.result[1][n] = e.y,
                o.result[2][n] = e.z
            })
        }
        return t.prototype.linkLength = function(t) {
            return t.actualLength(this.result)
        }
        ,
        t.prototype.start = function(t) {
            var e = this;
            void 0 === t && (t = 100);
            var n = this.nodes.length
              , s = new l;
            this.useJaccardLinkLengths && a.jaccardLinkLengths(this.links, s, 1.5),
            this.links.forEach(function(t) {
                return t.length *= e.idealLinkLength
            });
            var u = new r.Calculator(n,this.links,function(t) {
                return t.source
            }
            ,function(t) {
                return t.target
            }
            ,function(t) {
                return t.length
            }
            ).DistanceMatrix()
              , c = o.Descent.createSquareMatrix(n, function(t, e) {
                return u[t][e]
            })
              , f = o.Descent.createSquareMatrix(n, function() {
                return 2
            });
            this.links.forEach(function(t) {
                var e = t.source
                  , n = t.target;
                return f[e][n] = f[n][e] = 1
            }),
            this.descent = new o.Descent(this.result,c),
            this.descent.threshold = .001,
            this.descent.G = f,
            this.constraints && (this.descent.project = new i.Projection(this.nodes,null,null,this.constraints).projectFunctions());
            for (var h = 0; h < this.nodes.length; h++) {
                var d = this.nodes[h];
                d.fixed && this.descent.locks.add(h, [d.x, d.y, d.z])
            }
            return this.descent.run(t),
            this
        }
        ,
        t.prototype.tick = function() {
            this.descent.locks.clear();
            for (var t = 0; t < this.nodes.length; t++) {
                var e = this.nodes[t];
                e.fixed && this.descent.locks.add(t, [e.x, e.y, e.z])
            }
            return this.descent.rungeKutta()
        }
        ,
        t.dims = ["x", "y", "z"],
        t.k = t.dims.length,
        t
    }();
    e.Layout3D = c;
    var l = function() {
        function t() {}
        return t.prototype.getSourceIndex = function(t) {
            return t.source
        }
        ,
        t.prototype.getTargetIndex = function(t) {
            return t.target
        }
        ,
        t.prototype.getLength = function(t) {
            return t.length
        }
        ,
        t.prototype.setLength = function(t, e) {
            t.length = e
        }
        ,
        t
    }()
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = n(136)
      , o = n(195);
    e.gridify = function(t, e, n, r) {
        return t.cola.start(0, 0, 0, 10, !1),
        function(t, e, n, r) {
            t.forEach(function(t) {
                t.routerNode = {
                    name: t.name,
                    bounds: t.bounds.inflate(-n)
                }
            }),
            e.forEach(function(e) {
                e.routerNode = {
                    bounds: e.bounds.inflate(-r),
                    children: (void 0 !== e.groups ? e.groups.map(function(e) {
                        return t.length + e.id
                    }) : []).concat(void 0 !== e.leaves ? e.leaves.map(function(t) {
                        return t.index
                    }) : [])
                }
            });
            var i = t.concat(e).map(function(t, e) {
                return t.routerNode.id = e,
                t.routerNode
            });
            return new o.GridRouter(i,{
                getChildren: function(t) {
                    return t.children
                },
                getBounds: function(t) {
                    return t.bounds
                }
            },n - r)
        }(t.cola.nodes(), t.cola.groups(), n, r).routeEdges(t.powerGraph.powerEdges, e, function(t) {
            return t.source.routerNode.id
        }, function(t) {
            return t.target.routerNode.id
        })
    }
    ,
    e.powerGraphGridLayout = function(t, e, n) {
        var o;
        t.nodes.forEach(function(t, e) {
            return t.index = e
        }),
        (new r.Layout).avoidOverlaps(!1).nodes(t.nodes).links(t.links).powerGraphGroups(function(t) {
            (o = t).groups.forEach(function(t) {
                return t.padding = n
            })
        });
        var i = t.nodes.length
          , a = []
          , s = t.nodes.slice(0);
        return s.forEach(function(t, e) {
            return t.index = e
        }),
        o.groups.forEach(function(t) {
            var e = t.index = t.id + i;
            s.push(t),
            void 0 !== t.leaves && t.leaves.forEach(function(t) {
                return a.push({
                    source: e,
                    target: t.index
                })
            }),
            void 0 !== t.groups && t.groups.forEach(function(t) {
                return a.push({
                    source: e,
                    target: t.id + i
                })
            })
        }),
        o.powerEdges.forEach(function(t) {
            a.push({
                source: t.source.index,
                target: t.target.index
            })
        }),
        (new r.Layout).size(e).nodes(s).links(a).avoidOverlaps(!1).linkDistance(30).symmetricDiffLinkLengths(5).convergenceThreshold(1e-4).start(100, 0, 0, 0, !1),
        {
            cola: (new r.Layout).convergenceThreshold(.001).size(e).avoidOverlaps(!0).nodes(t.nodes).links(t.links).groupCompactness(1e-4).linkDistance(30).symmetricDiffLinkLengths(5).powerGraphGroups(function(t) {
                (o = t).groups.forEach(function(t) {
                    t.padding = n
                })
            }).start(50, 0, 100, 0, !1),
            powerGraph: o
        }
    }
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = i(n(2))
      , o = i(n(4));
    function i(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    var a = function() {
        function t(e, n) {
            (0,
            r.default)(this, t),
            this.exec = e,
            this.flag = !1,
            this.delay = n,
            this.time = 0
        }
        return (0,
        o.default)(t, [{
            key: "start",
            value: function() {
                var t = this;
                window.requestAnimationFrame(function() {
                    (t.time++,
                    t.time % t.delay == 0) ? t.flag ? t.stop() : t.exec() ? t.stop() : t.start() : t.start()
                })
            }
        }, {
            key: "stop",
            value: function() {
                this.exec = null,
                this.flag = null,
                this.delay = null
            }
        }]),
        t
    }();
    e.default = a
}
, function(module, exports, __webpack_require__) {
    "use strict";
    Object.defineProperty(exports, "__esModule", {
        value: !0
    });
    var _promise = __webpack_require__(19)
      , _promise2 = _interopRequireDefault(_promise)
      , _getPrototypeOf = __webpack_require__(16)
      , _getPrototypeOf2 = _interopRequireDefault(_getPrototypeOf)
      , _classCallCheck2 = __webpack_require__(2)
      , _classCallCheck3 = _interopRequireDefault(_classCallCheck2)
      , _createClass2 = __webpack_require__(4)
      , _createClass3 = _interopRequireDefault(_createClass2)
      , _possibleConstructorReturn2 = __webpack_require__(10)
      , _possibleConstructorReturn3 = _interopRequireDefault(_possibleConstructorReturn2)
      , _inherits2 = __webpack_require__(11)
      , _inherits3 = _interopRequireDefault(_inherits2)
      , _core = __webpack_require__(57)
      , _core2 = _interopRequireDefault(_core)
      , _ms = __webpack_require__(135)
      , _ms2 = _interopRequireDefault(_ms);
    function _interopRequireDefault(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    var WebService = function(_Service) {
        function WebService(t) {
            return (0,
            _classCallCheck3.default)(this, WebService),
            (0,
            _possibleConstructorReturn3.default)(this, (WebService.__proto__ || (0,
            _getPrototypeOf2.default)(WebService)).call(this, t))
        }
        return (0,
        _inherits3.default)(WebService, _Service),
        (0,
        _createClass3.default)(WebService, [{
            key: "pre_relation_company",
            value: function(t) {
                return this.get("/qq/" + t + ".json?random=" + Date.now())
            }
        }, {
            key: "query_relation_company",
            value: function query_relation_company(graphId) {
                var _this2 = this;
                return new _promise2.default(function(resolve, reject) {
                    _this2.pre_relation_company(graphId).then(function(res) {
                        for (var data = res.data, arr = data.v.split(","), fnStr = "", i = 0; i < arr.length; i++)
                            fnStr += String.fromCharCode(arr[i]);
                        if (eval(fnStr),
                        window.$SoGou$ = (0,
                        _ms2.default)(graphId),
                        window.wtf) {
                            for (var fxck = window.wtf().split(","), fxckStr = "", i = 0; i < fxck.length; i++)
                                fxckStr += window.$SoGou$[fxck[i]];
                            document.cookie = "_rutm=" + fxckStr + ";path=/;",
                            delete window.wtf
                        }
                        resolve(_promise2.default.resolve(_this2.get("/dis/getInfoById/" + graphId + ".json?")))
                    })
                }
                )
            }
        }, {
            key: "query_relation_human",
            value: function(t, e, n) {
                var r = this;
                return new _promise2.default(function(o, i) {
                    var a = {
                        "Content-Type": "application/json; charset=UTF-8"
                    };
                    n.version && (a.version = decodeURIComponent(n.version)),
                    n.token && (a["X-Auth-Token"] = n.token),
                    n.auth && (a.Authorization = n.auth);
                    var s = {
                        hid: t,
                        cid: e,
                        key: n.key,
                        time: n.time
                    };
                    n.mobile && (s.mobile = n.mobile),
                    o(_promise2.default.resolve(r.get("/dis/human.json", s, a)))
                }
                )
            }
        }, {
            key: "query_time_line",
            value: function(t) {
                return this.get("dis/timeline.json", {
                    id: t
                })
            }
        }, {
            key: "query_equity_tree",
            value: function(t, e, n) {
                return this.get("/dis/investorGraph/investorGraph.json", {
                    flag: e,
                    ids: t,
                    dir: n
                })
            }
        }, {
            key: "discover_getInvestRoot",
            value: function(t) {
                return this.get("/cloud-equity-provider/v4/equity/indexnode.json", {
                    id: t
                })
            }
        }, {
            key: "discover_getInvest",
            value: function(t, e, n, r) {
                return this.get("/cloud-equity-provider/v4/equity/nextnode.json", {
                    id: t,
                    indexId: e,
                    direction: n
                }, r)
            }
        }]),
        WebService
    }(_core2.default);
    exports.default = WebService
}
, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = m(n(32))
      , o = m(n(16))
      , i = m(n(2))
      , a = m(n(4))
      , s = m(n(10))
      , u = m(n(11))
      , c = n(12)
      , l = m(c)
      , f = m(n(114))
      , h = n(35)
      , d = m(n(188))
      , p = n(270);
    n(172);
    var v = m(n(174))
      , g = m(n(196))
      , y = (n(199),
    n(50));
    function m(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    var _ = (0,
    h.createStore)(d.default, (0,
    h.applyMiddleware)(h.thunk))
      , w = function(t) {
        function e() {
            return (0,
            i.default)(this, e),
            (0,
            s.default)(this, (e.__proto__ || (0,
            o.default)(e)).apply(this, arguments))
        }
        return (0,
        u.default)(e, t),
        (0,
        a.default)(e, [{
            key: "showLoading",
            value: function(t) {
                var e = this.state
                  , n = e.origin
                  , o = e.time;
                window.parent && n && window.parent.postMessage((0,
                r.default)({
                    action: "showLoading",
                    flag: t,
                    time: o
                }), n)
            }
        }, {
            key: "downloadGraph",
            value: function() {
                var t = this
                  , e = this.state
                  , n = (e.mobile,
                e.origin)
                  , o = (e.id,
                e.time);
                if (!this.isDownLoad) {
                    this.isDownLoad = !0;
                    var i = this.canvas.exportJSON()
                      , a = this.canvas.getRootName();
                    window.LZMA.compress(i, 5, function(e, i) {
                        if (i)
                            return console.log(i),
                            void (t.isDownLoad = !1);
                        (0,
                        y.downloadPng)({
                            data: e,
                            name: a
                        }).then(function(e) {
                            t.isDownLoad = !1,
                            "ok" === e.state && e.data && window.parent !== window && window.parent.postMessage((0,
                            r.default)({
                                action: "download-company",
                                url: e.data,
                                time: o
                            }), n)
                        })
                    }, function(t) {
                        console.log(t)
                    })
                }
            }
        }, {
            key: "downloadGraphSVG",
            value: function() {
                var t = this
                  , e = this.state
                  , n = (e.mobile,
                e.origin)
                  , o = (e.id,
                e.time);
                if (!this.isDownLoadSVG) {
                    this.isDownLoadSVG = !0;
                    var i = this.canvas.exportJSON()
                      , a = this.canvas.getRootName();
                    window.LZMA.compress(i, 5, function(e, i) {
                        if (i)
                            return console.log(i),
                            void (t.isDownLoadSVG = !1);
                        (0,
                        y.downloadSVG)({
                            data: e,
                            name: a
                        }).then(function(e) {
                            t.isDownLoadSVG = !1,
                            "ok" === e.state && e.data && window.parent !== window && window.parent.postMessage((0,
                            r.default)({
                                action: "download-company-svg",
                                data: e.data,
                                time: o
                            }), n)
                        }, function() {
                            t.isDownLoadSVG = !1,
                            window.parent !== window && window.parent.postMessage((0,
                            r.default)({
                                action: "download-company-svg",
                                time: o
                            }), n)
                        })
                    }, function(t) {
                        console.log(t)
                    })
                }
            }
        }, {
            key: "componentDidMount",
            value: function(t) {
                var e = x("ids")
                  , n = x("mobile") || ""
                  , r = x("time") || ""
                  , o = x("key") || ""
                  , i = x("origin") || ""
                  , a = x("full") || ""
                  , s = this;
                if (!e) {
                    var u = window.location.hash;
                    try {
                        e = (e = u.match(/ids=(\d+)(&|$)/)) ? e[1] : "",
                        n = (n = u.match(new RegExp("mobile=([^&]*)?(&|$)"))) ? n[1] : "",
                        r = (r = u.match(new RegExp("time=([^&]*)?(&|$)"))) ? r[1] : "",
                        o = (o = u.match(new RegExp("key=([^&]*)?(&|$)"))) ? o[1] : "",
                        i = (i = u.match(new RegExp("origin=([^&]*)?(&|$)"))) ? decodeURIComponent(i[1]) : "",
                        a = !!a
                    } catch (t) {
                        console.log(t)
                    }
                }
                this.setState({
                    id: e,
                    mobile: n,
                    time: r,
                    key: o,
                    origin: i
                });
                var c = this.refs.canvas;
                window._isFull = a,
                c.setAttribute("resize", !0),
                this.canvas = new p.CompanyRelation(c),
                this.canvas.setUp(e),
                this.canvas.dataBlockBuildHandler = function() {
                    s.showLoading(!1)
                }
                ,
                window.addEventListener && window.addEventListener("message", function(t) {
                    if (String(t.origin) === i && t.data) {
                        var e = JSON.parse(t.data);
                        if (String(e.time) !== r)
                            return;
                        "download" === e.action && this.downloadGraph(),
                        "download-svg" === e.action && this.downloadGraphSVG()
                    }
                }
                .bind(this), !1),
                window.downloadGraph = this.downloadGraph.bind(this),
                window.downloadGraphSVG = this.downloadGraphSVG.bind(this)
            }
        }, {
            key: "componentWillMount",
            value: function(t) {}
        }, {
            key: "render",
            value: function() {
                return l.default.createElement("div", {
                    className: "main pt-80"
                }, l.default.createElement("canvas", {
                    ref: "canvas",
                    className: "canvas-main"
                }), l.default.createElement(v.default, null), l.default.createElement(g.default, null))
            }
        }]),
        e
    }(c.Component);
    function x(t) {
        var e = new RegExp("(^|&)" + t + "=([^&]*)(&|$)","i")
          , n = window.location.search.substr(1).match(e);
        return null != n ? decodeURIComponent(n[2]) : window.location.hash.indexOf("?") && null != (n = window.location.hash.substr(window.location.hash.lastIndexOf("?")).substr(1).match(e)) ? decodeURIComponent(n[2]) : null
    }
    e.default = w,
    f.default.render(l.default.createElement(h.Provider, {
        store: _
    }, l.default.createElement(w, null)), document.getElementById("relation_ws"))
}
, function(t, e, n) {
    "use strict";
    var r = s(n(271))
      , o = s(n(221))
      , i = s(n(18))
      , a = s(n(126));
    function s(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    n(58),
    r.default.prototype.getService = function() {
        return new o.default(this.host)
    }
    ,
    t.exports = {
        CompanyRelation: r.default,
        Util: i.default,
        SaveUrl: (0,
        a.default)()
    }
}
, function(t, e, n) {
    "use strict";
    Object.defineProperty(e, "__esModule", {
        value: !0
    });
    var r = m(n(19))
      , o = m(n(162))
      , i = m(n(16))
      , a = m(n(2))
      , s = m(n(4))
      , u = m(n(10))
      , c = m(n(11))
      , l = m(n(209))
      , f = m(n(189))
      , h = m(n(211))
      , d = m(n(52))
      , p = m(n(212))
      , v = m(n(37))
      , g = n(213)
      , y = m(n(18));
    m(n(220));
    function m(t) {
        return t && t.__esModule ? t : {
            default: t
        }
    }
    var _ = v.default.Path
      , w = v.default.Shape
      , x = v.default.TycText
      , b = v.default.Point
      , k = v.default.Group
      , L = v.default.Raster
      , E = v.default.TycLinkGroup
      , S = v.default.TycNodeGroup
      , N = v.default.traceTycGroup
      , T = v.default.GroupStore
      , C = v.default.SymbolDefinition
      , M = v.default.TycPathCircle
      , I = v.default.TycSymbolCircle
      , O = v.default.TycSymbolLinePath
      , P = v.default.TycSymbolLinePoi
      , A = (v.default.TycCircleGroup,
    v.default.Size)
      , D = y.default.lineSplit
      , j = y.default.angle
      , G = y.default.lineCenter
      , R = y.default.lineLength
      , z = y.default.angleXY
      , F = function(t) {
        function e(t, n) {
            (0,
            a.default)(this, e);
            var r = (0,
            u.default)(this, (e.__proto__ || (0,
            i.default)(e)).call(this, t, n));
            return r.relationData = new f.default,
            r.groupStore = new T,
            r.sysTimeLog = new p.default,
            r.rasterStore = {},
            r._stopZoom = !0,
            r._zoomDelay = 1e3,
            r.symbols = {},
            r.initSymbol(),
            r
        }
        return (0,
        c.default)(e, t),
        (0,
        s.default)(e, [{
            key: "initSymbol",
            value: function() {
                var t = this.symbols;
                (0,
                o.default)(h.default).filter(function(t) {
                    return t.startsWith("node")
                }).forEach(function(e) {
                    var n = h.default[e]
                      , r = new _.Circle(new b(0,0),n.diameter);
                    r.visible = n.visible,
                    n.visible && (r.fillColor = n.color,
                    n["border-width"] && (r.strokeWidth = n["border-width"],
                    r.strokeColor = n["border-color"])),
                    t["node-" + e.toLowerCase()] = new C(r);
                    var i = parseInt(n.diameter) + parseInt(n["path-width"]);
                    if ((r = new _.Circle(new b(0,0),i)).visible = n["path-visible"],
                    n["path-visible"] && (r.strokeWidth = n["path-width"],
                    r.strokeColor = n["path-color"]),
                    t["node-path-" + e.toLowerCase()] = new C(r),
                    (0,
                    o.default)(n).find(function(t) {
                        return t.startsWith("hover-")
                    })) {
                        (r = new _.Circle(new b(0,0),n.diameter)).visible = n["hover-visible"],
                        n["hover-visible"] && (r.fillColor = n["hover-color"] || n.color,
                        n["hover-border-width"] && (r.strokeWidth = n["hover-border-width"] || n["border-width"],
                        r.strokeColor = n["hover-border-color"] || n["border-color"])),
                        t["node-hover-" + e.toLowerCase()] = new C(r);
                        var a = parseInt(n.diameter) + parseInt(n["hover-path-width"]) / 2 + parseInt(n["hover-border-width"]) / 2;
                        (r = new _.Circle(new b(0,0),a)).visible = n["hover-path-visible"],
                        n["hover-path-visible"] && (r.strokeWidth = n["hover-path-width"],
                        r.strokeColor = n["hover-path-color"]),
                        t["node-hover-path-" + e.toLowerCase()] = new C(r)
                    }
                }),
                (0,
                o.default)(h.default).filter(function(t) {
                    return t.startsWith("relationship")
                }).forEach(function(e) {
                    var n = h.default[e]
                      , r = new _("M-6,-2,L0,0,L-6,2Z");
                    if (r.strokeWidth = n["stroke-width"],
                    r.strokeColor = n.color,
                    r.fillColor = n.color,
                    t["link-poi-" + e.toLowerCase()] = new C(r),
                    (r = new _("M0,0L10,0")).strokeWidth = n["stroke-width"],
                    r.strokeColor = n.color,
                    t["link-" + e.toLowerCase()] = new C(r),
                    (0,
                    o.default)(n).find(function(t) {
                        return t.startsWith("hover-")
                    })) {
                        var i = new _("M-6,-2,L0,0,L-6,2Z");
                        i.strokeWidth = n["hover-stroke-width"] || n["stroke-width"],
                        i.strokeColor = n["hover-color"] || n.color,
                        i.fillColor = n["hover-color"] || n.color,
                        t["link-poi-hover-" + e.toLowerCase()] = new C(i),
                        (i = new _("M0,0L10,0")).strokeWidth = n["hover-stroke-width"] || n["stroke-width"],
                        i.strokeColor = n["hover-color"] || n.color,
                        t["link-hover-" + e.toLowerCase()] = new C(i)
                    }
                    (r = new _("M-6,-2,L0,0,L-6,2Z")).strokeWidth = n["stroke-width"],
                    r.strokeColor = n.color,
                    r.fillColor = n.color,
                    t["link-poi-opacity-" + e.toLowerCase()] = new C(r),
                    (r = new _("M0,0L10,0")).strokeWidth = n["stroke-width"],
                    r.strokeColor = n.color,
                    t["link-opacity-" + e.toLowerCase()] = new C(r)
                })
            }
        }, {
            key: "getSymbolCircle",
            value: function(t) {
                return t ? this.symbols["node-node." + t.toLowerCase()] ? this.symbols["node-node." + t.toLowerCase()] : (console.log("node-node." + t),
                this.symbols["node-node"]) : null
            }
        }, {
            key: "getSymbolPathCircle",
            value: function(t) {
                return t && this.symbols["node-path-node." + t.toLowerCase()] ? this.symbols["node-path-node." + t.toLowerCase()] : null
            }
        }, {
            key: "getSymbolLink939",
            value: function(t) {
                return t ? this.symbols["link-poi-relationship." + t.toLowerCase()] ? this.symbols["link-poi-relationship." + t.toLowerCase()] : (console.log("link-poi-relationship." + t.toLowerCase()),
                this.symbols["link-poi-relationship"]) : null
            }
        }, {
            key: "getSymbolLink",
            value: function(t) {
                return t ? this.symbols["link-relationship." + t.toLowerCase()] ? this.symbols["link-relationship." + t.toLowerCase()] : (console.log("link-relationship." + t.toLowerCase()),
                this.symbols["link-relationship"]) : null
            }
        }, {
            key: "getSymbolCircleHover",
            value: function(t) {
                return t && this.symbols["node-hover-node." + t.toLowerCase()] ? this.symbols["node-hover-node." + t.toLowerCase()] : null
            }
        }, {
            key: "getSymbolPathCircleHover",
            value: function(t) {
                return t && this.symbols["node-hover-path-node." + t.toLowerCase()] ? this.symbols["node-hover-path-node." + t.toLowerCase()] : null
            }
        }, {
            key: "getSymbolLink939Hover",
            value: function(t) {
                return t && this.symbols["link-poi-hover-relationship." + t.toLowerCase()] ? this.symbols["link-poi-hover-relationship." + t.toLowerCase()] : null
            }
        }, {
            key: "getSymbolLinkHover",
            value: function(t) {
                return t && this.symbols["link-hover-relationship." + t.toLowerCase()] ? this.symbols["link-hover-relationship." + t.toLowerCase()] : null
            }
        }, {
            key: "getSymbolCircleOpacity",
            value: function(t) {
                return t ? this.symbols["node-opacity-node." + t.toLowerCase()] ? this.symbols["node-opacity-node." + t.toLowerCase()] : (console.log("node-opacity-node." + t),
                this.getSymbolCircle(t)) : null
            }
        }, {
            key: "getSymbolLink939Opacity",
            value: function(t) {
                return t ? this.symbols["link-poi-relationship." + t.toLowerCase()] ? this.symbols["link-poi-relationship." + t.toLowerCase()] : (console.log("link-poi-relationship." + t.toLowerCase()),
                this.getSymbolLink939(t)) : null
            }
        }, {
            key: "getSymbolLinkOpacity",
            value: function(t) {
                return t ? this.symbols["link-relationship." + t.toLowerCase()] ? this.symbols["link-relationship." + t.toLowerCase()] : (console.log("link-relationship." + t.toLowerCase()),
                this.getSymbolLink(t)) : null
            }
        }, {
            key: "setUp",
            value: function(t) {
                this.graphId = t
            }
        }, {
            key: "initError",
            value: function() {}
        }, {
            key: "showMaskLayer",
            value: function(t) {
                var e = this.layerManager;
                this.showMaskState = t,
                e.showMaskLayer(t)
            }
        }, {
            key: "updateMaskLayer",
            value: function() {}
        }, {
            key: "sendToTopLayer",
            value: function(t) {}
        }, {
            key: "retry",
            value: function() {
                this.graphId && this.initData(this.graphId)
            }
        }, {
            key: "initData",
            value: function(t) {
                var e = this
                  , n = (this.canvasCenter,
                this.service)
                  , r = this.relationData;
                this.sysTimeLog.push("pre query"),
                n.query_relation_company(t).then(function(n) {
                    if ("warn" !== n.state) {
                        e.sysTimeLog.push("end query");
                        var o = n.data.nodes.find(function(e) {
                            return String(e.id) === String(t) && (e.fx = 0,
                            e.fy = 0,
                            e.isRoot = !0,
                            !0)
                        });
                        e.rootName = o.properties.name;
                        var i = n.data
                          , a = i.nodes
                          , s = i.relationships;
                        a.forEach(function(t) {
                            return e.warpNode(t)
                        }),
                        s.forEach(function(t) {
                            return e.warpLink(t)
                        }),
                        r.pushNodes(a),
                        r.pushLinks(s),
                        e.sysTimeLog.push("pre dataBlockBuild"),
                        e.dataBlockBuild().then(function() {
                            e.sysTimeLog.push("end dataBlockBuild"),
                            e.dataBlockBuildHandler(),
                            e.drawCanvas(),
                            e.execCanvasEvent(),
                            e.execImageCanvas()
                        })
                    } else
                        e.initError()
                }).catch(function(t) {
                    console.log(t),
                    e.initError(t)
                })
            }
        }, {
            key: "drawCanvas",
            value: function() {
                var t = this;
                this.clickHitGroup = null;
                var e = this.showNodes
                  , n = this.showLinks
                  , r = (this.dataBlock,
                this.canvasLayer,
                this.rootId);
                this.layerManager.canvasLayerRemoveAllChildren(),
                this.sysTimeLog.push("start drawLink"),
                n.forEach(function(e) {
                    t.drawLink(e)
                }),
                this.sysTimeLog.push("emd drawLink"),
                this.sysTimeLog.push("start drawNode"),
                e.forEach(function(e) {
                    t.drawNode(e, e.x, e.y)
                }),
                this.sysTimeLog.push("emd drawNode");
                var o = this.groupStore.match(r).nodes.find(function(t) {
                    return String(t.data.nodeId) == String(r)
                });
                this.hitGroup = o,
                this.clickHitGroup = o,
                window._isFull || this.clickNodeGroup(r)
            }
        }, {
            key: "drawNode",
            value: function(t, e, n) {
                var r = this.canvasLayer
                  , o = this.scaleLinearX
                  , i = this.scaleLinearY
                  , a = this.rasterStore
                  , s = this.viewScale
                  , u = 0
                  , c = 0
                  , l = new S;
                l.pivot = [0, 0];
                var f = void 0
                  , h = t.properties.name || t.properties.title
                  , d = parseInt(t.fontSize * s);
                if (a[String(t.id)] && a[String(t.id)].loaded) {
                    f = t.labels[0] + ".image";
                    var p = a[String(t.id)].clone();
                    p.size = new A(2 * t.radius * s,2 * t.radius * s),
                    p.position = new b(u,c),
                    p.visible = !0,
                    l.addChild(p);
                    var v = new I(this.getSymbolCircle(f));
                    l.addChild(v);
                    var g = new M(this.getSymbolPathCircle(f));
                    l.addChild(g),
                    v = null;
                    var y = new k;
                    if (y.pivot = [0, 0],
                    this.showFont) {
                        var m = h.length <= 3 ? h : h.substr(0, 3) + "..."
                          , _ = new x({
                            fontFamily: this.fontFamily,
                            point: new b(u * s,(c + 20) * s),
                            fontSize: d,
                            justification: "center",
                            fillColor: t.fillText,
                            content: m
                        })
                          , L = -_.bounds.width / 2
                          , E = new w.Rectangle(L,(c + 20 - (t.fontSize / 2 + 4)) * s,_.bounds.width,t.fontSize * s);
                        E.fillColor = "black",
                        E.opacity = .36,
                        y.addChild(E),
                        y.addChild(_)
                    }
                    l.addChild(y)
                } else {
                    f = t.labels[0] + (t.isRoot ? ".root" : "");
                    var N = new I(this.getSymbolCircle(f));
                    l.addChild(N);
                    var T = new M(this.getSymbolPathCircle(f));
                    l.addChild(T),
                    N = null;
                    var C = new k;
                    C.pivot = [0, 0],
                    this.showFont && (h.length <= 3 ? C.addChild(new x({
                        fontFamily: this.fontFamily,
                        point: new b(u * s,(c + 4) * s),
                        fontSize: d,
                        justification: "center",
                        fillColor: t.fillText,
                        content: h
                    })) : h.length > 3 && h.length <= 7 ? (C.addChild(new x({
                        fontFamily: this.fontFamily,
                        point: new b(u * s,(c - 4) * s),
                        fontSize: d,
                        justification: "center",
                        fillColor: t.fillText,
                        content: h.substr(0, 3)
                    })),
                    C.addChild(new x({
                        fontFamily: this.fontFamily,
                        point: new b(u * s,(c + 12) * s),
                        fontSize: d,
                        justification: "center",
                        fillColor: t.fillText,
                        content: h.substring(3)
                    }))) : h.length > 7 && (C.addChild(new x({
                        fontFamily: this.fontFamily,
                        point: new b(u * s,(c - 12) * s),
                        fontSize: d,
                        justification: "center",
                        fillColor: t.fillText,
                        content: h.substr(0, 3)
                    })),
                    C.addChild(new x({
                        fontFamily: this.fontFamily,
                        point: new b(u * s,(c + 4) * s),
                        fontSize: d,
                        justification: "center",
                        fillColor: t.fillText,
                        content: h.substr(3, 5)
                    })),
                    C.addChild(new x({
                        fontFamily: this.fontFamily,
                        point: new b(u * s,(c + 20) * s),
                        fontSize: d,
                        justification: "center",
                        fillColor: t.fillText,
                        content: h.length <= 11 ? h.substr(8, 3) : h.substr(8, 3) + "..."
                    })))),
                    l.addChild(C),
                    C = null
                }
                l.position = [o(e), i(n)],
                l.data = {
                    type: "node",
                    nodeType: f,
                    nodeId: t.id,
                    nodeModel: "",
                    radius: t.radius,
                    fillColor: t.fillColor,
                    strokeColor: t.strokeColor,
                    name: h
                },
                r.addChild(l),
                l.bringToFront(),
                this.groupStore.push(l),
                u = null,
                c = null,
                h = null,
                d = null
            }
        }, {
            key: "drawLink",
            value: function(t) {
                var e = this.canvasLayer
                  , n = this.relationGroup
                  , r = this.viewScale
                  , o = t.source
                  , i = t.target
                  , a = t.idSeq
                  , s = this.lineCenter(o, i)
                  , u = this.lineLength(o, i)
                  , c = j(o, i)
                  , l = 15 * r
                  , f = new E;
                f.pivot = new b(0,0);
                var h = n[a]
                  , d = t.properties.labels[0]
                  , p = 0
                  , v = void 0;
                h % 2 == 1 ? 1 === t.groupIndex || (v = Math.floor(t.groupIndex / 2),
                p = t.groupIndex % 2 == 1 ? v * l : -v * l) : (v = Math.ceil(t.groupIndex / 2),
                p = t.groupIndex % 2 == 1 ? (v - .5) * l : -(v - .5) * l),
                Math.abs(p) > Math.min(o.radius || 35, i.radius || 35) && (p = p / Math.abs(p) * Math.min(o.radius || 35, i.radius || 35),
                this.errorHandler("offset is out : " + t.id));
                var g = this.lineSplit(o.radius || 35, p)
                  , y = this.lineSplit(i.radius || 35, p);
                if (isNaN(-u / 2 + g) || isNaN(u / 2 - y))
                    this.errorHandler("path is nan : " + t.id);
                else {
                    var m = void 0;
                    (m = new O(this.getSymbolLink(t.type))).position = new b((g - y) / 2,0),
                    m.scale((u - g - y - 2) / 10, 1),
                    f.addChild(m),
                    (m = new P(this.getSymbolLink939(t.type))).position = new b(u / 2 - y - 5,0),
                    f.addChild(m);
                    var _ = new x({
                        fontFamily: this.fontFamily,
                        point: new b(0,(t.fontSize / 2 - 2.5) * r),
                        fontSize: t.fontSize * r,
                        justification: "center",
                        fillColor: t.fontColor,
                        content: d
                    })
                      , k = -_.bounds.width / 2
                      , L = new w.Rectangle(k,(-t.fontSize - 1) * r / 2,_.bounds.width,t.fontSize * r);
                    L.strokeWidth = 1,
                    L.strokeColor = "#ffffff",
                    L.strokeColor.opacity = 0,
                    L.fillColor = "#ffffff",
                    L.opacity = 0,
                    f.addChild(L),
                    f.addChild(_),
                    this.showFont || (_.visible = !1),
                    f.position = new b(s.x,s.y);
                    var S = z(c + 90, p);
                    f.translate([S.x, S.y]),
                    f.rotate(c),
                    c > 90 && c < 270 && f.children[3].rotate(-180),
                    e.addChild(f),
                    f.data = {
                        type: "link",
                        name: d,
                        idSeq: t.idSeq,
                        linkId: t.id,
                        linkType: t.type,
                        sourceId: o.id,
                        sourcePoi: {
                            x: o.x,
                            y: o.y,
                            radius: o.radius
                        },
                        targetId: i.id,
                        targetPoi: {
                            x: i.x,
                            y: i.y,
                            radius: i.radius
                        },
                        strokeColor: t.strokeColor,
                        offset: p,
                        fontSize: t.fontSize,
                        hoverFontSize: t.hoverFontSize,
                        fillText: t.fillText
                    },
                    f.sendToBack(),
                    this.groupStore.push(f),
                    o = null,
                    i = null,
                    a = null,
                    s = null,
                    u = null,
                    c = null,
                    l = null,
                    f = null,
                    h = null,
                    d = null,
                    p = null,
                    v = null,
                    m = null,
                    _ = null
                }
            }
        }, {
            key: "dataBlockBuild",
            value: function() {
                var t = this
                  , e = this.showNodes
                  , n = this.showLinks
                  , o = this.dataBlock
                  , i = this.canvasBlock
                  , a = (this.showCenter,
                this.layerManager);
                return this.relationGroup = this.execRelationGroup(e, n),
                new r.default(function(r, s) {
                    t.execLayout(e, n).then(function() {
                        t.dataBlockNull(),
                        n.forEach(function(t) {
                            (void 0 === o.maxX || o.maxX < t.source.x) && (o.maxX = t.source.x),
                            (void 0 === o.minX || o.minX > t.source.x) && (o.minX = t.source.x),
                            (void 0 === o.maxY || o.maxY < t.source.y) && (o.maxY = t.source.y),
                            (void 0 === o.minY || o.minY > t.source.y) && (o.minY = t.source.y),
                            (void 0 === o.maxX || o.maxX < t.target.x) && (o.maxX = t.target.x),
                            (void 0 === o.minX || o.minX > t.target.x) && (o.minX = t.target.x),
                            (void 0 === o.maxY || o.maxY < t.target.y) && (o.maxY = t.target.y),
                            (void 0 === o.minY || o.minY > t.target.y) && (o.minY = t.target.y)
                        }),
                        o.w = o.maxX - o.minX,
                        o.h = o.maxY - o.minY,
                        o.centerX = (o.maxX + o.minX) / 2,
                        o.centerY = (o.maxY + o.minY) / 2;
                        var s = Math.min(i.w / o.w, i.h / o.h);
                        s < .1 || e.length > 500 || n.length > 1e3 ? (a.canvasLayerScale(s, new b(i.w / 2,i.h / 2)),
                        t.layerScale = t.canvasLayer.scaling.x) : (t.layerScale = 1,
                        a.canvasLayerTranslate(new b(i.w / 2,i.h / 2))),
                        s = null,
                        r()
                    })
                }
                )
            }
        }, {
            key: "execLayout_far",
            value: function(t, e) {
                var n = this;
                return new r.default(function(r, o) {
                    var i = n.simulation;
                    i.nodes(t),
                    i.force("link").links(e),
                    i.stop();
                    for (var a = 0, s = 0, u = Math.ceil(Math.log(i.alphaMin()) / Math.log(1 - i.alphaDecay())); s < u && (a++,
                    i.tick(),
                    !(a > 100)); ++s)
                        ;
                    r()
                }
                )
            }
        }, {
            key: "execLayoutFisrtLevel",
            value: function(t, e) {
                for (var n = this.rootId, i = {}, a = [], s = 0; s < e.length; s++) {
                    var u = e[s];
                    u.startNode != n && u.endNode != n || (i[u.startNode] || (i[u.startNode] = t[u.startNode]),
                    i[u.endNode] || (i[u.endNode] = t[u.endNode]),
                    a.push(u))
                }
                return i = (0,
                o.default)(i).map(function(t) {
                    return i[t]
                }),
                new r.default(function(t, e) {
                    var n = (0,
                    g.d3adaptor)(d.default);
                    n.nodes(i).links(a).linkDistance(150).start(50);
                    for (var r = Date.now(), o = 300; o-- && Date.now() - r < 1500; ) {
                        if (.1 != n.alpha() && n.alpha() < 100) {
                            console.log("cola stop", Date.now() - r),
                            n.stop();
                            break
                        }
                        n.tick()
                    }
                    console.log("cola stop", Date.now() - r),
                    n.stop(),
                    i.forEach(function(t) {
                        t.fixed = !0
                    }),
                    t()
                }
                )
            }
        }, {
            key: "execLayout",
            value: function(t, e) {
                var n = this;
                return new r.default(function(r, o) {
                    for (var i = {}, a = 0; a < t.length; a++)
                        t[a].height = 75,
                        t[a].width = 75,
                        i[t[a].id] = t[a];
                    for (a = 0; a < e.length; a++) {
                        var s = e[a];
                        s.source = i[s.startNode],
                        s.target = i[s.endNode]
                    }
                    n.execLayoutFisrtLevel(i, e).then(function() {
                        var n = (0,
                        g.d3adaptor)(d.default)
                          , o = Date.now();
                        n.nodes(t).links(e).symmetricDiffLinkLengths(45).jaccardLinkLengths(210, .9).avoidOverlaps(!0).start(30, 20),
                        console.log("start cola time", Date.now() - o),
                        n.on("tick", function() {
                            if (n.alpha() < 800 && .1 != n.alpha())
                                return console.log("total time", Date.now() - o),
                                n.stop(),
                                void r()
                        })
                    })
                }
                )
            }
        }, {
            key: "execRelationGroup",
            value: function(t, e) {
                var n = {};
                return e.forEach(function(t) {
                    t.type.toLowerCase(),
                    t.targetId,
                    t.sourceId;
                    n[t.idSeq] || (n[t.idSeq] = 0),
                    n[t.idSeq] += 1,
                    t.groupIndex = n[t.idSeq]
                }),
                n
            }
        }, {
            key: "warpLink",
            value: function(t) {
                var e = this.linkStyle(t);
                t.strokeColor = e.color,
                t.fontColor = e["font-color"],
                t.fontSize = e["font-size"] || 10,
                t.hoverFontSize = e["hover-font-size"] || 12
            }
        }, {
            key: "warpNode",
            value: function(t) {
                var e = this.canvasCenter
                  , n = this.pathDepth;
                if (t) {
                    var r = this.nodeStyle(t);
                    t.fillColor = r.color,
                    t.strokeWidth = r["border-width"],
                    t.colorFull = r.color,
                    t.radius = parseInt(r.diameter),
                    t.fillText = r["font-color"],
                    t.strokeColor = r["border-color"],
                    t.fontSize = r["font-size"] || 10,
                    t.isStart ? t.fx = e.x - 130 * (n / 2 + 1) : t.isEnd && (t.fx = e.x + 130 * (n / 2 + 1)),
                    r = null
                }
            }
        }, {
            key: "linkStyle",
            value: function(t) {
                var e = this.canvasStyle;
                if (t.type) {
                    var n = t.type;
                    if (e["relationship." + n.toLowerCase()])
                        return e["relationship." + n.toLowerCase()]
                }
                return e["relationship.invest"]
            }
        }, {
            key: "nodeStyle",
            value: function(t) {
                var e = this.canvasStyle
                  , n = "";
                if (t.isRoot && (n = ".root"),
                t.labels && t.labels[0]) {
                    var r = t.labels[0];
                    if (e["node." + r.toLowerCase() + n])
                        return e["node." + r.toLowerCase() + n]
                }
                return e["node.company"]
            }
        }, {
            key: "dataBlockNull",
            value: function() {
                delete this._dataBlock.w,
                delete this._dataBlock.h,
                delete this._dataBlock.centerX,
                delete this._dataBlock.centerY,
                delete this._dataBlock.minX,
                delete this._dataBlock.minY,
                delete this._dataBlock.maxX,
                delete this._dataBlock.maxY
            }
        }, {
            key: "lineCenter",
            value: function(t, e) {
                var n = this.scaleLinearX
                  , r = this.scaleLinearY;
                return G({
                    x: n(t.x),
                    y: r(t.y)
                }, {
                    x: n(e.x),
                    y: r(e.y)
                })
            }
        }, {
            key: "lineLength",
            value: function(t, e) {
                var n = this.scaleLinearX
                  , r = this.scaleLinearY;
                return R({
                    x: n(t.x),
                    y: r(t.y)
                }, {
                    x: n(e.x),
                    y: r(e.y)
                })
            }
        }, {
            key: "lineSplit",
            value: function(t, e) {
                var n = this.viewScale;
                return D(t, e) * n
            }
        }, {
            key: "angle",
            value: function(t, e) {
                return j(t, e)
            }
        }, {
            key: "changeCanvasCursor",
            value: function(t) {
                d.default.select(this.canvas).style("cursor", t)
            }
        }, {
            key: "changeCanvasTitle",
            value: function(t) {
                t = t || "",
                d.default.select(this.canvas).attr("title", t)
            }
        }, {
            key: "startTimer",
            value: function() {
                var t = this;
                d.default.timeout(function() {
                    t.enableZoom()
                }, this._zoomDelay)
            }
        }, {
            key: "enableZoom",
            value: function() {
                this._stopZoom = !1
            }
        }, {
            key: "disableZoom",
            value: function() {
                this._stopZoom = !0
            }
        }, {
            key: "execCanvasEvent",
            value: function() {
                var t = this
                  , e = this.layerManager
                  , n = this;
                this.view.minDistance = 10,
                d.default.select(this.canvas).on("wheel.zoom", function() {
                    t._stopZoom || (event && event.preventDefault(),
                    t.zoomed(event))
                }),
                d.default.select(this.canvas).on("mouseenter", function() {
                    t.startTimer()
                }).on("mouseleave", function() {
                    t.disableZoom()
                }),
                this.tyc_event_state = "normal",
                this.tyc_event_timer = null,
                this.view.onMouseDown = function(t) {
                    console.log("down")
                }
                ,
                this.view.onMouseUp = function(r) {
                    console.log("up"),
                    t.tyc_event_timer && clearTimeout(t.tyc_event_timer),
                    "drag" === t.tyc_event_state && (t.tyc_event_timer = setTimeout(function() {
                        if (!n.clickHitGroup) {
                            var o = t.groupStore.nodes()
                              , i = t.groupStore.links();
                            t.showMaskLayer(!1),
                            i.forEach(function(e) {
                                e.changeState(t)
                            }),
                            o.forEach(function(e) {
                                e.changeState(t)
                            })
                        }
                        t.tyc_event_state = "drag_release",
                        t.dragHitGroup = null,
                        e.canvasLayerHitTest(r.point) || t.changeCanvasCursor("-webkit-grab")
                    }, 1))
                }
                ,
                this.view.onMouseDrag = function(e) {
                    console.log("drag"),
                    t.tyc_event_state = "drag",
                    e.stopPropagation(),
                    t.onViewDrag(e.point, e.delta)
                }
                ,
                this.view.onMouseMove = function(e) {
                    e.stopPropagation(),
                    "drag" !== t.tyc_event_state && (console.log("move"),
                    t.onViewMouseMove(e.point))
                }
                ,
                this.view.onClick = function(e) {
                    e.stopPropagation(),
                    "drag" !== t.tyc_event_state && t.onViewClick(e.point)
                }
                ,
                this.view.onDoubleClick = function(e) {
                    e.stopPropagation(),
                    t.onViewDoubleClick(e.point)
                }
            }
        }, {
            key: "zoomed",
            value: function(t) {
                var e = this.layerManager
                  , n = this.canvasLayer.scaling.x;
                n < .25 && t.deltaY > 0 || n > 2 && t.deltaY < 0 || (t.deltaY > 0 ? e.canvasLayerScale(.95, new b(t.x,t.y)) : e.canvasLayerScale(1.03, new b(t.x,t.y)))
            }
        }, {
            key: "onViewMouseMove",
            value: function(t) {
                var e = this.layerManager;
                if (this.clickHitGroup) {
                    var n = e.activeLayer.hitTest(t);
                    if (!n)
                        return;
                    var r = N(n.item, 4);
                    this.hitGroup && this.hitGroup === r || (this.mouseInGroup(r, !0),
                    this.changeCanvasCursor("pointer"))
                } else {
                    var o = e.canvasLayerHitTest(t);
                    if (o) {
                        var i = N(o.item, 4);
                        this.hitGroup && this.hitGroup === i || (this.mouseInGroup(i),
                        this.changeCanvasCursor("pointer")),
                        o = null,
                        i = null
                    } else
                        this.clickHitGroup || this.hitGroup && (this.mouseOutGroup(this.hitGroup),
                        this.hitGroup = null,
                        this.changeCanvasCursor("-webkit-grab"),
                        this.changeCanvasTitle(""))
                }
            }
        }, {
            key: "onViewDoubleClick",
            value: function(t) {
                var e = this.relationData
                  , n = this.layerManager.canvasLayerHitTest(t);
                if (n) {
                    var r = N(n.item, 4);
                    if (r instanceof S) {
                        var o = r.data.nodeType
                          , i = r.data.nodeId;
                        e.getNode(i);
                        if ("company" === o.toLowerCase())
                            this.clickCompany(i);
                        else if ("human.image" === o.toLowerCase()) {
                            var a = e.getLinks(i)[0]
                              , s = a.endNode;
                            a.endNode === i && (s = a.startNode),
                            this.clickHuman(i, s)
                        }
                        console.log("jump")
                    }
                }
            }
        }, {
            key: "onViewClick",
            value: function(t) {
                console.log("click");
                this.relationData;
                var e = this.layerManager
                  , n = this
                  , r = e.canvasLayerHitTest(t);
                if (!r)
                    return console.log("!hitRes"),
                    void (this.clickHitGroup && this.cancelClickGroup());
                var o = N(r.item, 4);
                if (o instanceof S)
                    if (this.clickHitGroup) {
                        var i = o.data.nodeId
                          , a = this.clickHitGroup.data.nodeId
                          , s = this.groupStore.match(a)
                          , u = s.nodes
                          , c = (s.links,
                        s.exclude);
                        c.nodes,
                        c.links;
                        u.find(function(t) {
                            return String(t.data.nodeId) == String(i)
                        }) ? (e.sendAllBackToBase(),
                        u.forEach(function(t) {
                            t.changeState(n, "normal")
                        }),
                        this.clickGroup(o)) : this.cancelClickGroup()
                    } else
                        this.clickGroup(o);
                else
                    this.clickHitGroup && this.cancelClickGroup()
            }
        }, {
            key: "onViewDrag",
            value: function(t, e) {
                this.maskRect,
                this.showMaskState;
                var n = this.layerManager;
                if (this.dragHitGroup)
                    this.nodeDrag(this.dragHitGroup, t);
                else {
                    var r = n.canvasLayerHitTest(t);
                    if (r) {
                        var o = N(r.item, 4);
                        o instanceof S ? (this.nodeDrag(o, t),
                        this.dragHitGroup = o,
                        this.changeCanvasCursor("pointer")) : (n.canvasLayerTranslate(e),
                        this.changeCanvasCursor("-webkit-grabbing"))
                    } else
                        n.canvasLayerTranslate(e)
                }
            }
        }, {
            key: "mouseInGroup",
            value: function(t, e) {
                this.hitGroup = t,
                t && (t instanceof S ? this.mouseInNode(t.data.nodeId, e) : t instanceof E && (e || t.changeState(this, "hover")))
            }
        }, {
            key: "mouseOutGroup",
            value: function(t) {
                t instanceof S ? this.mouseLeaveNode(t.data.nodeId) : t instanceof E && t.changeState(this)
            }
        }, {
            key: "mouseInNode",
            value: function(t, e) {
                var n = this
                  , r = (this.showCenter,
                this.canvasCenter,
                this.groupStore.match(t))
                  , o = r.nodes
                  , i = r.links
                  , a = r.exclude
                  , s = a.nodes
                  , u = a.links;
                if (e) {
                    var c = o.find(function(e) {
                        return e.data.nodeId === t
                    });
                    c.data && "Company" == c.data.nodeType && c.data.name && c.data.name.length > 11 ? this.changeCanvasTitle(c.data.name) : this.changeCanvasTitle("")
                } else
                    i.forEach(function(t) {
                        t.changeState(n, "hover")
                    }),
                    o.forEach(function(e) {
                        e.data.nodeId === t ? (e.changeState(n, "hover"),
                        e.data && "Company" == e.data.nodeType && e.data.name && e.data.name.length > 11 ? n.changeCanvasTitle(e.data.name) : n.changeCanvasTitle("")) : e.changeState(n)
                    }),
                    s.forEach(function(t) {
                        t.changeState(n)
                    }),
                    u.forEach(function(t) {
                        t.changeState(n)
                    })
            }
        }, {
            key: "clickGroup",
            value: function(t) {
                this.hitGroup = t,
                this.clickHitGroup = t,
                t && (t instanceof S ? this.clickNodeGroup(t.data.nodeId) : t instanceof E && (t.strokeWidth = 4))
            }
        }, {
            key: "cancelClickGroup",
            value: function() {
                var t = this.clickHitGroup;
                this.clickHitGroup = null,
                this.hitGroup = null,
                t instanceof S ? this.cancelClickNodeGroup(t.data.nodeId) : t instanceof E && (t.strokeWidth = 1)
            }
        }, {
            key: "clickNodeGroup",
            value: function(t) {
                var e = this;
                this.showMaskLayer(!0);
                this.showCenter,
                this.canvasCenter;
                var n = this.layerManager
                  , r = this.groupStore.match(t)
                  , o = r.nodes
                  , i = r.links
                  , a = r.exclude
                  , s = a.nodes
                  , u = a.links;
                i.forEach(function(t) {
                    t.changeState(e, "hover"),
                    n.sendToActive(t)
                }),
                o.forEach(function(r) {
                    r.data.nodeId === t ? r.changeState(e, "hover") : r.changeState(e),
                    n.sendToActive(r)
                }),
                s.forEach(function(t) {
                    t.changeState(e, "opacity")
                }),
                u.forEach(function(t) {
                    t.changeState(e, "opacity")
                })
            }
        }, {
            key: "cancelClickNodeGroup",
            value: function() {
                var t = this;
                this.showMaskLayer(!1);
                var e = this.groupStore.nodes();
                this.groupStore.links().forEach(function(e) {
                    e.changeState(t)
                }),
                e.forEach(function(e) {
                    e.changeState(t)
                }),
                this.cancelClickCompany()
            }
        }, {
            key: "nodeDrag",
            value: function(t, e) {
                var n = this
                  , r = this.groupStore.match(t.data.nodeId)
                  , o = r.nodes
                  , i = r.links
                  , a = r.exclude
                  , s = a.nodes
                  , u = a.links
                  , c = this.showNodes
                  , l = this.showLinks
                  , f = (this.groupStore,
                this.layerManager)
                  , h = (this.scaleLinearX,
                this.scaleLinearY,
                this.viewScale)
                  , d = this.canvasLayer.globalToLocal(e)
                  , p = t.data.nodeId;
                this.clickHitGroup || (this.showMaskLayer(!0),
                i.forEach(function(t) {
                    t.changeState(n, "hover"),
                    f.sendToActive(t)
                }),
                o.forEach(function(t) {
                    String(t.data.nodeId) === String(p) ? t.changeState(n, "hover") : t.changeState(n),
                    f.sendToActive(t)
                }),
                s.forEach(function(t) {
                    t.changeState(n, "opacity")
                }),
                u.forEach(function(t) {
                    t.changeState(n, "opacity")
                })),
                t.position = d,
                t.x = d.x,
                t.y = d.y,
                i.forEach(function(t) {
                    var e = t.data;
                    e.sourceId === p ? (e.sourcePoi.x = d.x,
                    e.sourcePoi.y = d.y) : e.targetId === p && (e.targetPoi.x = d.x,
                    e.targetPoi.y = d.y);
                    var r = e.sourcePoi
                      , o = e.targetPoi
                      , i = e.offset
                      , a = (e.strokeColor,
                    e.fillText)
                      , s = e.name
                      , u = e.hoverFontSize;
                    t.pivot = [0, 0],
                    t.removeChildren();
                    var c = n.lineCenter(r, o)
                      , l = n.lineLength(r, o)
                      , f = j(r, o)
                      , v = n.lineSplit(r.radius, i)
                      , g = n.lineSplit(o.radius, i)
                      , y = void 0;
                    (y = "hover" === t.tyc_hover_state ? new O(n.getSymbolLinkHover(e.linkType)) : new O(n.getSymbolLink(e.linkType))).position = new b((v - g) / 2,0),
                    y.scale((l - v - g - 2) / 10, 1),
                    t.addChild(y),
                    (y = "hover" === t.tyc_hover_state ? new P(n.getSymbolLink939Hover(e.linkType)) : new P(n.getSymbolLink939(e.linkType))).position = new b(l / 2 - g - 5,0),
                    t.addChild(y);
                    var m = new x({
                        fontFamily: n.fontFamily,
                        point: new b(0,(u / 2 - 2.5) * h),
                        fontSize: u * h,
                        justification: "center",
                        fillColor: a,
                        content: s
                    })
                      , _ = -m.bounds.width / 2
                      , k = new w.Rectangle(_,(-u - 1) * h / 2,m.bounds.width,u * h);
                    k.strokeWidth = 1,
                    k.strokeColor = "#ffffff",
                    k.strokeColor.opacity = 0,
                    k.fillColor = "#ffffff",
                    k.opacity = 1,
                    "opacity" === t.tyc_hover_state && (k.opacity = 0),
                    n.showFont || (m.visible = !1),
                    "opacity" === t.tyc_hover_state && (m.visible = !1),
                    t.addChild(k),
                    t.addChild(m),
                    f > 90 && f < 270 && t.children[3].rotate(-180),
                    t.position = new b(c.x,c.y);
                    var L = z(f + 90, i);
                    t.translate([L.x, L.y]),
                    t.rotate(f)
                }),
                l.forEach(function(t) {
                    t.source.id === p ? (t.source.x = d.x,
                    t.source.y = d.y) : t.target.id === p && (t.target.x = d.x,
                    t.target.y = d.y)
                });
                var v = c.find(function(t) {
                    return t.nodeId == p
                });
                v && (v.x = d.x,
                v.y = d.y)
            }
        }, {
            key: "mouseLeaveNode",
            value: function(t) {
                var e = this
                  , n = this.groupStore.nodes();
                this.groupStore.links().forEach(function(t) {
                    t.changeState(e)
                }),
                n.forEach(function(t) {
                    t.changeState(e)
                })
            }
        }, {
            key: "clickCompany",
            value: function(t) {
                window.open("https://www.tianyancha.com/company/" + t)
            }
        }, {
            key: "clickHuman",
            value: function(t, e) {
                window.open("https://www.tianyancha.com/human/" + t + "-c" + e)
            }
        }, {
            key: "cancelClickCompany",
            value: function() {}
        }, {
            key: "size",
            value: function() {
                var t = this.canvasLayer.strokeBounds;
                return {
                    w: t.width,
                    h: t.height,
                    x: t.x,
                    y: t.y
                }
            }
        }, {
            key: "reCalculateRectByText",
            value: function(t, e) {
                var n = this.viewScale
                  , r = new x({
                    fontFamily: this.fontFamily,
                    point: new b(0,0),
                    fontSize: e * n,
                    justification: "center",
                    content: t
                })
                  , o = -r.bounds.width / 2
                  , i = new w.Rectangle(o,-e * n / 2,r.bounds.width,e * n);
                return i.strokeWidth = 1,
                i.strokeColor = "#ffffff",
                i.strokeColor.opacity = 0,
                i.fillColor = "#ffffff",
                i.opacity = 1,
                r.remove(),
                i
            }
        }, {
            key: "nodeLogo",
            value: function(t) {
                var e = this.rasterStore
                  , n = [];
                return new r.default(function(r, o) {
                    var i = 0
                      , a = 0
                      , s = !1;
                    t.forEach(function(t) {
                        if ("Human" === t.labels[0]) {
                            var o = t.properties.logo;
                            if (o) {
                                o = o.indexOf("://") > -1 ? (o = o.replace("http://", "https://")).replace("watermark01", "t07") : "https://img5.tianyancha.com/" + t.properties.logo + "@!t03";
                                var u = new L({
                                    crossOrigin: "anonymous",
                                    source: o
                                });
                                a++,
                                u.onError = function() {
                                    ++i === a && s && r(n)
                                }
                                ,
                                u.onLoad = function() {
                                    ++i === a && s && r(n)
                                }
                                ,
                                u.visible = !1,
                                e[String(t.id)] = u,
                                n.push(t)
                            }
                        }
                    }),
                    s = !0,
                    i === a && s && r(n)
                }
                )
            }
        }, {
            key: "execImageCanvas",
            value: function() {
                var t = this
                  , e = this.showNodes;
                this.nodeLogo(e).then(function(e) {
                    e.forEach(function(t) {
                        t.radius = 35
                    }),
                    t.drawCanvas()
                })
            }
        }, {
            key: "getRootName",
            value: function() {
                return this.rootName ? this.rootName : ""
            }
        }, {
            key: "dataBlockBuildHandler",
            value: function() {}
        }, {
            key: "graphId",
            get: function() {
                return this._graphId
            },
            set: function(t) {
                this.sysTimeLog.push("graphId"),
                this._graphId = t,
                this.rootId = t,
                t && this.initData(t)
            }
        }, {
            key: "simulatio2n",
            get: function() {
                if (!this._simulation) {
                    var t = d.default.forceLink().id(function(t) {
                        return t.id
                    }).distance(function(t) {
                        return 130
                    })
                      , e = d.default.forceManyBody().strength(-2e3);
                    this._simulation = d.default.forceSimulation().force("link", t).force("charge", e).force("center", d.default.forceCenter(0, 0))
                }
                return this._simulation
            }
        }, {
            key: "simulation",
            get: function() {
                var t = this;
                if (!this._simulation) {
                    var e = d.default.forceLink().id(function(t) {
                        return t.id
                    }).distance(function(t) {
                        return 100
                    }).strength(function(e) {
                        return 1 / Math.max(t.relationGroup[e.idSeq])
                    })
                      , n = d.default.forceManyBody().strength(-1500);
                    d.default.forceCollide().strength(.6).radius(function(e) {
                        return 2 * Math.sqrt(t.relationData.getLinks(e.id).length)
                    });
                    this._simulation = d.default.forceSimulation().force("link", e).force("charge", n)
                }
                return this._simulation
            }
        }, {
            key: "showNodes",
            get: function() {
                return this.relationData.nodes
            }
        }, {
            key: "showLinks",
            get: function() {
                return this.relationData.links
            }
        }, {
            key: "canvasStyle",
            get: function() {
                return this._canvasStyle || h.default
            },
            set: function(t) {
                this._canvasStyle = t
            }
        }, {
            key: "dataBlock",
            get: function() {
                return this._dataBlock || (this._dataBlock = {}),
                this._dataBlock
            }
        }, {
            key: "showFont",
            get: function() {
                return void 0 === this._showFont && (this._showFont = 1),
                this._showFont
            }
        }, {
            key: "layerScale",
            get: function() {
                return this._layerScale
            },
            set: function(t) {
                t < .5 && this.showFont ? this._showFont = 0 : t > .5 && !this.showFont && (this._showFont = 1),
                this._layerScale = t
            }
        }, {
            key: "showCenter",
            get: function() {
                return this._showCenter || {
                    x: 0,
                    y: 0
                }
            },
            set: function(t) {
                this._showCenter = t
            }
        }, {
            key: "fontFamily",
            get: function() {
                return "Microsoft YaHei"
            }
        }]),
        e
    }(l.default);
    e.default = F
}
]);
