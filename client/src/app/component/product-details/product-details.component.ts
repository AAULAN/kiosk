import { Component, OnInit, Input } from '@angular/core';
import { Product } from 'src/app/model/product.model';

@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html'
})
export class ProductDetailsComponent implements OnInit {
  @Input() product: Product;

  constructor() { }

  ngOnInit() {
    if (!this.product.id) {
      console.log(this.product);
    }
  }
}
