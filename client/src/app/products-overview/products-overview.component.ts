import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-products-overview',
  templateUrl: './products-overview.component.html',
  styleUrls: ['./products-overview.component.scss']
})
export class ProductsOverviewComponent implements OnInit {
  displayedColumns: string[] = ['name', 'price', 'actions'];
  products = [];

  constructor() { }

  ngOnInit() {
    this.products = [{'name': 'test', 'price': 12}];
  }
}
